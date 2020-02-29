from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from utils.db import get_db
from service import user as user_service
from dto.user import User, Credentials
from security.authenticate import authenticate, get_current_user
from security import jwt

router = APIRouter()


@router.post("/register/", response_model=User)
def register(
        *,
        db: Session = Depends(get_db),
        user_in: Credentials
):
    """
    Register User
    """
    user = user_service.find_by_email(db, user_email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user already exists in the system.",
        )
    user = user_service.create(db, user_in=user_in)

    return user


@router.post("/login/", response_model=jwt.Token)
def login(
        *,
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends(),
):
    """
    Login User
    """
    user = authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password",
        )

    return {
        "access_token": jwt.create_access_token(
            data={"user_id": user.id}
        )
    }
