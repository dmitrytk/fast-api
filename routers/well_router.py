from fastapi import APIRouter

from db.models import WellModel, WellInModel
from services import well_service

router = APIRouter()


@router.get("/{well_id}", tags=["wells"])
async def read_well(field_id: int, well_id: int):
    return await well_service.read_well(field_id, well_id)


@router.post("/", tags=["wells"], response_model=WellModel)
async def post_well(field_id: int, well: WellInModel):
    return await well_service.post_well(field_id, well)


@router.delete("/{well_id}", tags=["wells"])
async def delete_well(field_id: int, well_id: int):
    return await well_service.delete_well(field_id, well_id)
