from fastapi import APIRouter

from app.web import (
    task as tasks
)

api_router = APIRouter()
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
