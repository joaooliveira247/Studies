from fastapi import FastAPI
from core.config import settings
from api.v1.api import api_router


app = FastAPI(title="Courses API")
app.include_router(api_router, prefix=settings.API_VERSION_PATH)
