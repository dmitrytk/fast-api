from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routers import field_router, well_router

app = FastAPI()

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


register_tortoise(
    app,
    db_url="sqlite://./app.db",
    modules={"models": ["db.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
