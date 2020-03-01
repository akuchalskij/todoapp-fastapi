from fastapi import APIRouter

from app.web import (
    user_controller as users,
    task_controller as tasks
)

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["auth"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
