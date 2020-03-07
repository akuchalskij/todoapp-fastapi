from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from config import settings
from config.db import Database
from routes.api import api_router

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Database.Session()
    response = await call_next(request)
    request.state.db.close()

    return response
