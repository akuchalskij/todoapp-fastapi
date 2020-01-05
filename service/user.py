from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from entity.user import User
from dao.user import UserCreate
from utils.security import get_password_hash


def find_by_id(db_session: Session, *, user_id: int) -> Optional[User]:
    return db_session.query(User).filter(User.id == user_id).first()


def find_by_email(db_session: Session, *, user_email: str) -> Optional[User]:
    return db_session.query(User).filter(User.email == user_email).first()


def find_all(db_session: Session, *, skip=0, limit=100) -> List[Optional[User]]:
    return db_session.query(User).offset(skip).limit(limit).all()


def create(db_session: Session, *, user_in: UserCreate) -> User:
    user = User(
        email=user_in.email,
        password=get_password_hash(user_in.password),
        full_name=user_in.full_name
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
