from fastapi import APIRouter, Depends

from dto.user import User as UserDTO
from entity.user import User
from security.authenticate import get_current_user

router = APIRouter()


@router.get("/me/", response_model=UserDTO)
def read_user_me(current_user: User = Depends(get_current_user)):
    """
    Get current user.
    """
    return current_user
