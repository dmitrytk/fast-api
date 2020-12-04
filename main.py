from fastapi import FastAPI
from tortoise import Tortoise

from routers import field_router, well_router
from utils import populate, initdb

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await initdb()
    await populate()


@app.on_event("shutdown")
async def shutdown_event():
    await Tortoise.close_connections()


app.include_router(field_router.router,
                   prefix="/fields",
                   tags=["fields"],
                   )

app.include_router(well_router.router,
                   prefix="/fields/{field_id}/wells",
                   tags=["wells"],
                   )


@app.get("/")
def home():
    return {'message': 'Hello world!'}
