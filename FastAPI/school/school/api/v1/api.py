from fastapi import APIRouter
from .routers import article, user

api_router: APIRouter = APIRouter()

api_router.include_router(
    article.router, prefix="/articles", tags=["Articles"]
)
api_router.include_router(user.router, prefix="users", tags=["Users"])
