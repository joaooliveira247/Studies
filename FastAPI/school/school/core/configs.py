from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_VERSION: str = "0.1.0"
    __API_PATH_VERSION: int = 1
    API_PATH: str = f"/api/v{__API_PATH_VERSION}"
    DB_URL: str = (
        "postgresql+asyncpg://postgres_pub:passwd@localhost:5432/courses"
    )
    DB_BASEMODEL = declarative_base()
    NAME: str = "New York Times Articles API"
    DESCRIPTION: str = "An api to managment NYT articles"

    JWT_SECRET: str = "PmU9jLFYEsuMAj9uYko27Q9HZ2cMWWM4KHv5Iph3J9w"
    # look lib secrets
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    class Config:
        case_sensitive: bool = True


settings: Settings = Settings()
