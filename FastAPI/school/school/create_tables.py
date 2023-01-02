from school.core.configs import settings
from school.core.database import engine


async def create_tables() -> None:
    import school.models.__all_models

    print("Creating tables into database ...")

    try:
        async with engine.begin() as conn:
            await conn.run_sync(settings.DB_BASEMODEL.metadata.drop_all)
            await conn.run_sync(settings.DB_BASEMODEL.metadata.create_all)
    except Exception as e:
        raise Exception(f"Error while try create tables: {e}")
    print("Tables created with sucess.")
