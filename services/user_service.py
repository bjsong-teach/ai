# services/user_service.py

from typing import Dict, Any, Optional
from datetime import timedelta
import json
import time

from fastapi import HTTPException, status
from redis.asyncio import Redis 

from crud import (
    create_user, get_user_by_email, get_user_by_username, get_user_by_id,
    update_user, update_user_password, verify_password, get_password_hash
)
from auth import create_access_token, decode_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from schemas import UserCreate, UserResponse, UserUpdate, PasswordChange, Token

class UserService:
    def __init__(self, redis_client: Redis):
        self.redis_client = redis_client

    async def register_new_user(self, user_create: UserCreate) -> UserResponse:
        cached_email_exists = await self.redis_client.get(f"email_exists:{user_create.email}")
        if cached_email_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        cached_username_exists = await self.redis_client.get(f"username_exists:{user_create.username}")
        if cached_username_exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )

        if get_user_by_email(user_create.email):
            await self.redis_client.setex(f"email_exists:{user_create.email}", 3600, "1")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        if get_user_by_username(user_create.username):
            await self.redis_client.setex(f"username_exists:{user_create.username}", 3600, "1")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )

        user_data = create_user(user_create.username, user_create.email, user_create.password)

        user_cache_key = f"user:{user_data['id']}"
        await self.redis_client.setex(user_cache_key, 3600, json.dumps(user_data))
        await self.redis_client.setex(f"email_exists:{user_create.email}", 3600, "1")
        await self.redis_client.setex(f"username_exists:{user_create.username}", 3600, "1")

        return UserResponse(id=user_data["id"], username=user_data["username"], email=user_data["email"])

    async def authenticate_user(self, username: str, password: str, request_ip: str) -> Token:
        login_attempt_key = f"login_attempts:{request_ip}"
        max_attempts = 5
        window_seconds = 60

        attempts = await self.redis_client.incr(login_attempt_key)
        if attempts == 1:
            await self.redis_client.expire(login_attempt_key, window_seconds)
        elif attempts > max_attempts:
            ttl = await self.redis_client.ttl(login_attempt_key)
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f"Too many login attempts. Please try again after {ttl} seconds."
            )

        user = get_user_by_username(username)
        if not user or not verify_password(password, user["hashed_password"]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user["username"], "id": user["id"]},
            expires_delta=access_token_expires
        )

        await self.redis_client.delete(login_attempt_key)

        user_cache_key = f"user:{user['id']}"
        user['last_login'] = int(time.time())
        await self.redis_client.setex(user_cache_key, 3600, json.dumps(user))

        return {"access_token": access_token, "token_type": "bearer"}

    async def get_current_user_info(self, user_id: int) -> Dict[str, Any]:
        user_cache_key = f"user:{user_id}"
        cached_user_json = await self.redis_client.get(user_cache_key)
        if cached_user_json:
            print("User data fetched from Redis cache.")
            return json.loads(cached_user_json)

        user_data = get_user_by_id(user_id)
        if not user_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        await self.redis_client.setex(user_cache_key, 3600, json.dumps(user_data))
        print("User data fetched from DB and cached.")
        return user_data

    async def update_user_profile(self, user_id: int, current_user_email: str, current_user_username: str, user_update: UserUpdate) -> UserResponse:
        if user_update.email and user_update.email != current_user_email:
            if get_user_by_email(user_update.email):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        if user_update.username and user_update.username != current_user_username:
            if get_user_by_username(user_update.username):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken")

        updated_user_data = update_user(
            user_id=user_id,
            username=user_update.username,
            email=user_update.email
        )
        if not updated_user_data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update user"
            )

        await self.redis_client.delete(f"user:{user_id}")
        if user_update.email and user_update.email != current_user_email:
            await self.redis_client.delete(f"email_exists:{current_user_email}")
            await self.redis_client.setex(f"email_exists:{user_update.email}", 3600, "1")
        if user_update.username and user_update.username != current_user_username:
            await self.redis_client.delete(f"username_exists:{current_user_username}")
            await self.redis_client.setex(f"username_exists:{user_update.username}", 3600, "1")

        return UserResponse(
            id=updated_user_data["id"],
            username=updated_user_data["username"],
            email=updated_user_data["email"]
        )

    async def change_user_password(self, user_id: int, old_password: str, new_password: str, current_hashed_password: str):
        if not verify_password(old_password, current_hashed_password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect old password"
            )

        new_hashed_password = get_password_hash(new_password)
        updated_user = update_user_password(user_id, new_hashed_password)

        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to change password"
            )

        await self.redis_client.set(f"password_changed_at:{user_id}", int(time.time()))
        await self.redis_client.delete(f"user:{user_id}")

        return {"message": "Password changed successfully"}