from functools import lru_cache

from fastapi import FastAPI, Depends

import config

app = FastAPI()


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
def read_root():
    return {"Hello": "World "}


@app.get("/info")
async def info(settings: config.Settings = Depends(get_settings)):
    return {
        "app_name": settings.postgres_user,
    }
