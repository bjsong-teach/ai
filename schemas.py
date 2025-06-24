# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi import Form # as_form 메서드를 위해 추가

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        email: EmailStr = Form(...),
        password: str = Form(...)
    ):
        return cls(username=username, email=email, password=password)

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    id: Optional[int] = None # 토큰에 id를 포함시키기 위해 추가

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None

class PasswordChange(BaseModel):
    old_password: str
    new_password: str