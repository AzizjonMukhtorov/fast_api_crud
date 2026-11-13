from fastapi import HTTPException, status

from ..db.database import Session
from ..schemas.auth import RegisterRequest

from ..repositories.auth import get_user_by_username, register_user, get_users
from ..auth.security import verify_password, create_access_token

def register_user_service(db: Session, data: RegisterRequest):
    if get_user_by_username(db, data.username):
        raise HTTPException(status_code=409, detail="Username already exists")
    
    user = register_user(db, data)
    return user

def login_user_service(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    
    if user is None or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {'access_token': create_access_token(user.id)}

def get_users_service(db: Session):
    users = get_users(db)
    
    return users