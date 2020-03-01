from fastapi import APIRouter

from web import user_controller,  task_controller

api_router = APIRouter()
api_router.include_router(user_controller.router, prefix="/users", tags=["auth"])
api_router.include_router(task_controller.router, prefix="/tasks", tags=["tasks"])
