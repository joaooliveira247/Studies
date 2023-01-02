from fastapi import FastAPI
from school.core.configs import settings
from school.api.v1.api import api_router


app: FastAPI = FastAPI(
    title=settings.NAME,
    description=settings.DESCRIPTION,
    version=settings.API_VERSION,
)
app.include_router(api_router, prefix=settings.API_PATH)
