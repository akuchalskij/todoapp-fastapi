from typing import Optional

import jwt
from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from passlib.context import CryptContext
from starlette.status import HTTP_403_FORBIDDEN

from config import settings
from app.dto import Credentials
from app.entity import User
from app.repository import UserRepository
from app.security import ALGORITHM, TokenPayload

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, *, request: Credentials) -> User:
        user = User(
            email=request.email,
            password=pwd_context.hash(request.password),
        )

        return self.repository.save(user)

    def authenticate(self, *, email: str, password: str) -> Optional[User]:
        user = self.repository.find_by(entity_class=User, entity_param=User.email, variable=email)

        if not user:
            return None

        if not pwd_context.verify(password, user.password):
            return None

        return user

    def get_current_user(self, token: str = Security(reusable_oauth2)):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
            token_data = TokenPayload(**payload)
        except PyJWTError:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
            )

        user = self.repository.find_by(entity_class=User, entity_param=User.id, variable=token_data.user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user
