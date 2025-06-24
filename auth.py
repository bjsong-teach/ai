# auth.py
import os
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from jose import JWTError, jwt
from passlib.context import CryptContext

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from redis.asyncio.cluster import RedisCluster
from database import get_redis_client

SECRET_KEY = os.getenv("SECRET_KEY", "your-default-insecure-secret-key-change-it-now")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "iat": datetime.utcnow()}) # 'iat' (issued at) 클레임 추가
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        issued_at: int = payload.get("iat")
        user_id: int = payload.get("id") # 추가된 id 클레임
        if username is None or issued_at is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials: Missing payload data",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return {"username": username, "iat": issued_at, "id": user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials: Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    redis_client: RedisCluster = Depends(get_redis_client)
) -> Dict[str, Any]:
    token_data = decode_access_token(token)
    username = token_data["username"]
    token_issued_at = token_data["iat"]
    user_id = token_data["id"]

    from crud import get_user_by_username, get_user_by_id

    user = get_user_by_username(username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    password_changed_at_str = await redis_client.get(f"password_changed_at:{user['id']}")
    if password_changed_at_str:
        password_changed_at = int(password_changed_at_str)
        if token_issued_at < password_changed_at:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Password has been changed. Please log in again.",
                headers={"WWW-Authenticate": "Bearer"},
            )
    return user