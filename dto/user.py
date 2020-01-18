from typing import Optional, Dict, Any

from pydantic import BaseModel


class UserBase(BaseModel):
    email: Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int = None


class Credentials(User):
    email: str
    password: str
