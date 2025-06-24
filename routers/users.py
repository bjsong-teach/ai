# routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordRequestForm
from typing import Dict, Any
from redis.asyncio.cluster import RedisCluster # RedisCluster 타입 임포트
from schemas import UserCreate, UserResponse, Token, UserUpdate, PasswordChange
from database import get_redis_client
from services.user_service import UserService # 서비스 계층 임포트
from auth import get_current_user # 현재 사용자 가져오는 의존성 (여전히 필요)

templates = Jinja2Templates(directory="templates")
router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# UserService 인스턴스를 의존성 주입으로 제공하는 헬퍼 함수
async def get_user_service(
    redis_client: RedisCluster = Depends(get_redis_client)
) -> UserService:
    return UserService(redis_client)

# --- HTML 폼 제공 엔드포인트 ---

@router.get("/register", response_class=HTMLResponse)
async def get_register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
async def get_login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# --- API 엔드포인트 (서비스 계층 호출) ---

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_create: UserCreate = Depends(UserCreate.as_form),
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.register_new_user(user_create)

@router.post("/login", response_model=Token)
async def login_for_access_token(
    request: Request, # <- 이 부분을 가장 위로 올립니다.
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: UserService = Depends(get_user_service)
):
    request_ip = request.client.host if request.client else "unknown"
    return await user_service.authenticate_user(form_data.username, form_data.password, request_ip)

@router.get("/me", response_model=UserResponse)
async def read_users_me(
    current_user: Dict[str, Any] = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service) # 사실 여기서는 현재 current_user 정보를 그대로 반환하므로 service 호출이 필수는 아님
):
    # current_user는 이미 auth.py에서 Redis를 거쳐 검증된 사용자 정보를 가져옴.
    # UserResponse 스키마에 맞춰 반환
    return UserResponse(
        id=current_user["id"],
        username=current_user["username"],
        email=current_user["email"]
    )


@router.put("/me", response_model=UserResponse)
async def update_users_me(
    user_update: UserUpdate,
    current_user: Dict[str, Any] = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.update_user_profile(
        user_id=current_user["id"],
        current_user_email=current_user["email"],
        current_user_username=current_user["username"],
        user_update=user_update
    )

@router.post("/me/change-password")
async def change_password_me(
    password_change: PasswordChange,
    current_user: Dict[str, Any] = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.change_user_password(
        user_id=current_user["id"],
        old_password=password_change.old_password,
        new_password=password_change.new_password,
        current_hashed_password=current_user["hashed_password"]
    )