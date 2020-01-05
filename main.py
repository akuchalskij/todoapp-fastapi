from typing import List

import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
import databases

from config import settings
from routes.api import api_router

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1)

