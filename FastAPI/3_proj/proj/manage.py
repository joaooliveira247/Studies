from sys import argv
import subprocess
from core.config import settings
from core.data_base import engine


async def create_tables() -> None:
    import models.__all_models
    print("Criando as tabelas no banco de dados ...")

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBASEMODEL.metadata.drop_all)
        await conn.run_sync(settings.DBBASEMODEL.metadata.create_all)
    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    import uvicorn
    import asyncio

    if argv[1] == "create-table":
        asyncio.run(create_tables())
    if argv[1] == "start":
        uvicorn.run("main:app", port=8000, log_level="info", reload=True)
    if argv[1] == "docker-up":
        subprocess.run("docker compose up -d", shell=True)
