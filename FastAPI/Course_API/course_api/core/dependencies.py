from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from course_api.core.database import Session


async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session

    except Exception as e:
        raise Exception(f"error {e} in session from dependencies.")

    finally:
        await session.close()
