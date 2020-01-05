from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from utils.db import get_db
from service import user as user_service
from dao.user import User, UserCreate

router = APIRouter()


@router.post("/users/", response_model=User)
def create_user(
        *,
        db: Session = Depends(get_db),
        user_in: UserCreate
):
    """
    Create new user.
    """
    user = user_service.find_by_email(db, user_email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, user_in=user_in)

    return user
