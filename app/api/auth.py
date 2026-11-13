from typing import Annotated

from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from ..schemas.auth import (RegisterRequest, UserResponse,
                            TokenResponse)
from ..auth.dependencies import DB, AdminUser, CurrentUser
from ..services.auth import register_user_service, login_user_service, get_users_service



auth_router = APIRouter(tags=['Auth'])



@auth_router.post("/register", response_model=UserResponse, status_code=201)
def register(data: RegisterRequest, db: DB):
    return register_user_service(db, data)

@auth_router.post("/login", response_model=TokenResponse)
def login(
    form: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: DB,
):
    return login_user_service(db, form.username, form.password)   

@auth_router.get("/users/me", response_model=UserResponse)
def read_me(current_user: CurrentUser):
    return current_user

@auth_router.get("/admin/users", response_model=list[UserResponse])
def list_users(db: DB, admin: AdminUser):
    return get_users_service(db)