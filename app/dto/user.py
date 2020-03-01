from typing import Optional

from pydantic import BaseModel


class UserDTOBase(BaseModel):
    email: Optional[str] = None

    class Config:
        orm_mode = True


class UserDTO(UserDTOBase):
    id: int = None


class Credentials(UserDTO):
    email: str
    password: str
