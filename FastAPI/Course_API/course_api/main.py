from fastapi import FastAPI
from course_api.api.v1.api import api_router
from course_api.core.config import settings

app: FastAPI = FastAPI(
    title=settings.NAME,
    description=settings.DESCRIPTION,
    version=settings.API_VERSION,
)
app.include_router(api_router, prefix=settings.API_PATH)


routes: list = app.router.routes
