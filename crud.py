# crud.py
from typing import Dict, Any, Optional
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

_users_db: Dict[int, Dict[str, Any]] = {}
_next_user_id = 1

def create_user(username: str, email: str, password: str) -> Dict[str, Any]:
    global _next_user_id
    hashed_password = get_password_hash(password)
    user = {
        "id": _next_user_id,
        "username": username,
        "email": email,
        "hashed_password": hashed_password
    }
    _users_db[_next_user_id] = user
    _next_user_id += 1
    return user

def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
    for user_id, user_data in _users_db.items():
        if user_data["email"] == email:
            return user_data
    return None

def get_user_by_username(username: str) -> Optional[Dict[str, Any]]:
    for user_id, user_data in _users_db.items():
        if user_data["username"] == username:
            return user_data
    return None

def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    return _users_db.get(user_id)

def update_user(user_id: int, username: Optional[str] = None, email: Optional[str] = None) -> Optional[Dict[str, Any]]:
    user = _users_db.get(user_id)
    if user:
        if username is not None:
            user["username"] = username
        if email is not None:
            user["email"] = email
        return user
    return None

def update_user_password(user_id: int, new_password_hash: str) -> Optional[Dict[str, Any]]:
    user = _users_db.get(user_id)
    if user:
        user["hashed_password"] = new_password_hash
        return user
    return None