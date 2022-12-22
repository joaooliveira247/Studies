from sqlmodel import SQLModel
from course_api.core.database import engine


async def create_tables() -> None:
    import course_api.models.__all_models

    print("Creating tables into database ...")

    try:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)
            await conn.run_sync(SQLModel.metadata.create_all)
    except Exception as e:
        raise Exception(f"Error while try create tables: {e}")
    print("Tables created with sucess.")
