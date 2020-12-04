from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from db.models import WellModel, Well, WellInModel, Field


async def read_well(field_id: int, well_id: int) -> WellModel:
    try:
        well = await Well.get(pk=well_id, field_id=field_id)
        return await WellModel.from_tortoise_orm(well)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Well not found")


async def post_well(field_id: int, well: WellInModel) -> WellModel:
    field = await Field.get(pk=field_id)
    well = await Well.create(field=field, **well.dict(exclude_unset=True))
    return await WellModel.from_tortoise_orm(well)


async def delete_well(field_id: int, well_id: int) -> dict:
    deleted_count = await Well.filter(field_id=field_id, pk=well_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Well {well_id} not found")
    return {'message': f'Deleted well {well_id}'}
