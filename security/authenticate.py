from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from utils.security import get_password_hash, verify_password
from entity.user import User
from dto.user import Credentials
from service.user import find_by_email


def authenticate(db_session: Session, *, email: str, password: str) -> Optional[User]:
    user = find_by_email(db_session, user_email=email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
