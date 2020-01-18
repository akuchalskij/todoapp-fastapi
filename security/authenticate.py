from typing import Optional

import jwt
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from sqlalchemy.orm import Session
from starlette.status import HTTP_403_FORBIDDEN

from config import settings
from entity.user import User
from security.jwt import ALGORITHM, TokenPayload
from service.user import find_by_email, find_by_id
from utils.db import get_db
from utils.security import verify_password

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/")


def authenticate(db_session: Session, *, email: str, password: str) -> Optional[User]:
    user = find_by_email(db_session, user_email=email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def get_current_user(db: Session = Depends(get_db), token: str = Security(reusable_oauth2)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    user = find_by_id(db, user_id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
