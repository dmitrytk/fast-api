from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.testclient import TestClient
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "World"})


@app.get("/hello")
def hello(request: Request):
    return {'message': 'Hello world!'}


@app.post("/fields/", response_model=schemas.Field)
def create_field(field: schemas.FieldCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_field(db=db, field=field)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Field with this name already exists")


@app.post("/fields/create")
def delete_all_fields(db: Session = Depends(get_db)):
    return crud.bulk_create_fields(db)


@app.delete("/fields/")
def delete_all_fields(db: Session = Depends(get_db)):
    return crud.delete_all_fields(db)


@app.get("/fields/{field_id}", response_model=schemas.Field)
def read_field(field_id: int, db: Session = Depends(get_db)):
    field = crud.get_field(field_id=field_id, db=db)
    return field


@app.get("/fields/", response_model=List[schemas.Field])
def read_fields(db: Session = Depends(get_db)):
    fields = crud.get_fields(db)
    return fields


@app.delete("/fields/{field_id}")
def delete_field(field_id: int, db: Session = Depends(get_db)):
    return crud.delete_field(field_id, db)


@app.get("/sandbox")
def sandbox():
    return {'message': 'sandbox'}


@app.post("/sandbox", response_model=List[schemas.WellCreate])
def sandbox(data: List[schemas.WellCreate]):
    print(len(data))
    return data


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
