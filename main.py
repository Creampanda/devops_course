from fastapi import FastAPI
import uvicorn
from app.config import PORT
from app.routers import router

app = FastAPI()

app.include_router(router)


def start():
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    start()
