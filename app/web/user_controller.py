from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from app.dto import UserDTO, Credentials
from app.entity import User
from app.repository import UserRepository
from app.security import Token, create_access_token
from app.service import UserService
from app.web import BaseController

router = APIRouter()


class UserController(BaseController):
    def __init__(self, service: UserService, repository: UserRepository):
        self.service = service
        self.repository = repository

    @router.post("/register/", response_model=UserDTO)
    def register(self, request: Credentials):
        """
        Register User
        """
        user = self.repository.find_by(entity_class=User, entity_param=User.email, variable=request.email)

        if user:
            raise HTTPException(status_code=400, detail="The user already exists in the system.")

        user = self.service.create(request=request)

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
