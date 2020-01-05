from fastapi import APIRouter

from web import user

api_router = APIRouter()
api_router.include_router(user.router, tags=["user"])
