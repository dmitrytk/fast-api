from fastapi import HTTPException

from db.models import FieldModel, Field, FieldInModel, Well, WellModel


# BASIC CRUD
async def get_field(field_id: int) -> FieldModel:
    return await FieldModel.from_queryset_single(Field.get(id=field_id))


async def get_fields():
    return await FieldModel.from_queryset(Field.all())


async def post_field(field: FieldInModel):
    field_obj = await Field.create(**field.dict(exclude_unset=True))
    return await FieldModel.from_tortoise_orm(field_obj)


async def delete_field(field_id):
    deleted_count = await Field.filter(id=field_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {field_id} not found")
    return {'message': f'Deleted field {field_id}'}


# CHILD OBJECTS
async def read_wells(field_id: int):
    return await WellModel.from_queryset(Well.filter(field_id=field_id))
