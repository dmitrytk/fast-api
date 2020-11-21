from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {'message':'home'}


@app.post("/fields/", response_model=schemas.Field)
def create_field(field: schemas.FieldCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_field(db=db, field=field)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Field with this name already exists")


@app.get("/fields/", response_model=List[schemas.Field])
def read_fields(db: Session = Depends(get_db)):
    fields = crud.get_fields(db)
    return fields
