from pydantic import BaseSettings


class Settings(BaseSettings):
    API_VERSION: str = "0.1.0"
    __API_PATH_VERSION: int = 1
    API_PATH: str = f"/api/v{__API_PATH_VERSION}"
    DB_URL: str = (
        "postgresql+asyncpg://postgres_pub:passwd@localhost:5432/courses"
    )
    NAME: str = "Course API"
    DESCRIPTION: str = "An api to management your courses"

    class Config:
        case_sensitive: bool = True


settings = Settings()
