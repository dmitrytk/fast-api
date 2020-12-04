from fastapi import APIRouter

from db.models import FieldInModel
from services import field_service

router = APIRouter()


@router.get("/", tags=["fields"])
async def read_fields():
    return await field_service.get_fields()


@router.get("/{id}", tags=["fields"])
async def read_field(id: int):
    return await field_service.get_field(id)


@router.post("/", tags=["fields"])
async def post_field(field: FieldInModel):
    return await field_service.post_field(field)


@router.delete("/{id}", tags=["fields"])
async def post_field(id: int):
    return await field_service.delete_field(id)


# CHILD OBJECTS
@router.get("/{id}/wells", tags=["fields"])
async def read_wells(id: int):
    return await field_service.read_wells(id)
