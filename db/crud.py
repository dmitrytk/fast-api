from typing import List

from sqlalchemy.orm import Session

from . import models, schemas


def get_fields(db: Session) -> List[models.Field]:
    return db.query(models.Field).all()


def get_field(field_id: int, db: Session) -> models.Field:
    field = db.query(models.Field).filter(models.Field.id == field_id).first()
    print(field)
    return field


def delete_field(id: int, db: Session):
    return db.query(models.Field).filter(models.Field.id == id).delete()


def create_field(db: Session, field: schemas.FieldCreate):
    db_field = models.Field(name=field.name)
    db.add(db_field)
    db.commit()
    db.refresh(db_field)
    return db_field


def bulk_create_fields(db: Session):
    fields = []
    for i in range(100):
        field = models.Field(name=f'Field{i}')
        fields.append(field)
    db.bulk_save_objects(fields)
    db.commit()


def delete_all_fields(db: Session):
    count = db.query(models.Field).delete()
    db.commit()
    return count
