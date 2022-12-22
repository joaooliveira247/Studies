from course_api.create_tables import create_tables
from sys import argv
from pathlib import Path
import subprocess
import asyncio
import uvicorn
from pprint import pprint
from course_api.main import routes

def main(args: list[str]) -> None:
    match args[0]:
        case "run":
            uvicorn.run(
                "course_api.main:app",
                host="0.0.0.0",
                port=8000,
                log_level="info",
                reload=True
            )
            return
        case "create-table":
            asyncio.run(create_tables())
            return
        case "docker-run":
            if not Path("./docker-compose.yml").exists():
                raise Exception(
                    f"docker-compose.yml not found in {Path('./').absolute()}"
                )
            subprocess.run(
                "docker compose -f/home/virusxd/Projects/Studies/FastAPI/"
                "3_proj/docker-compose.yml up -d",
                shell=True,
            )
            return
        case "test":
            raise NotImplementedError("This will be implmented yet.")
        case "route":
            pprint(routes)
            return
    raise Exception("Command not found.")


if __name__ == "__main__":
    main(argv[1:])
    # print(Path("./docker-compose.yml").exists())
