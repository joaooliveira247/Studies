from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_VERSION_PATH: str = "/api/v1"
    DB_URL = (
        "postgresql+asyncpg://postgres_pub:passwd@localhost:5432/courses"
        )
    DBBASEMODEL = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
