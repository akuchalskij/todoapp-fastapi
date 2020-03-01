from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from dto.user import User, Credentials
from entity import User as UserEntity
from repository import UserRepository
from security import Token, create_access_token
from service import UserService
from web import BaseController

router = APIRouter()


class UserController(BaseController):
    def __init__(self, service: UserService, repository: UserRepository):
        self.service = service
        self.repository = repository

    @router.post("/register/", response_model=User)
    def register(self, request: Credentials) -> User:
        """
        Register User
        """
        user = self.repository.find_by(
            entity_class=UserEntity, entity_param=UserEntity.email, variable=request.email
        )

        if user:
            raise HTTPException(status_code=400, detail="The user already exists in the system.")

        user = self.service.create(user_in=request)

        return user

    @router.post("/login/", response_model=Token)
    def login(self, form_data: OAuth2PasswordRequestForm = Depends()):
        """
        Login User
        """
        user = self.service.authenticate(email=form_data.username, password=form_data.password)

        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")

        return {
            "access_token": create_access_token(data={"user_id": user.id})
        }
