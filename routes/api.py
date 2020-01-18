from fastapi import APIRouter

from web import auth, user, tasks

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/users", tags=["user"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
