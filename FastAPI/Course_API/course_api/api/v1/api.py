from fastapi import APIRouter
from course_api.core.config import settings
from course_api.api.v1.endpoints.course import router


api_router: APIRouter = APIRouter()
api_router.include_router(router, prefix="/courses", tags=["Courses"])
