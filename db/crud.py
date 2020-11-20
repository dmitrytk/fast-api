from sqlalchemy.orm import Session

from . import models, schemas


def get_fields(db: Session):
    return db.query(models.Field).all()


def create_field(db: Session, field: schemas.FieldCreate):
    db_field = models.Field(name=field.name)
    db.add(db_field)
    db.commit()
    db.refresh(db_field)
    return db_field
