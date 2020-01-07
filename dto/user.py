from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: Optional[str] = None


class User(UserBase):
    id: int = None


class Credentials(User):
    email: str
    password: str
