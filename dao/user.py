from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None


class User(UserBase):
    id: int = None


class UserCreate(User):
    email: str
    password: str
