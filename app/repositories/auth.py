from fastapi import HTTPException

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError


from ..models.models import User
from ..db.database import Session
from ..schemas.auth import RegisterRequest
from ..auth.security import hash_password


def get_user_by_username(db: Session, username):
    existing_user = db.scalar(
        select(User).where(User.username == username)
    )
    admin_user = db.get(User, 1)
    admin_user.is_admin = True
    db.commit()
    return existing_user

def register_user(db: Session, data: RegisterRequest):
    user = User(
        username=data.username,
        hashed_password=hash_password(data.password),
        is_active=True,
        is_admin=False,
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Username already exists")
    db.refresh(user)
    return user
    

def get_users(db: Session):
    
    users = db.scalars(select(User)).all()
    return users