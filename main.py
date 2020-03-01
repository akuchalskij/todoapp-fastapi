from fastapi import FastAPI
from starlette.requests import Request

from config import settings, db
from routes.api import api_router

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = db.Session()
    response = await call_next(request)
    request.state.db.close()

    return response
