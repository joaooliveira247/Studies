from fastapi import FastAPI
import uvicorn

app: FastAPI = FastAPI()


@app.get("/")
async def root():
    return {
        "msg": "First API with FastAPI."
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="localhost", port=8000, log_level="info", reload=True
        )

# gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker