from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist
from src.database.models import Appartment
from src.schemas.appartments import AppartmentOutSchema, AppartmentInSchema, UpdateAppartment


async def get_appartments():
    return await AppartmentOutSchema.from_queryset(Appartment.all())


async def get_appartment(appartment_id: int) -> AppartmentOutSchema:
    return await AppartmentOutSchema.from_queryset_single(Appartment.get(id=appartment_id))

async def create_appartment(appartment: AppartmentInSchema) -> AppartmentOutSchema:
    appartment_dict = appartment.model_dump(exclude_unset=True)
    appartment_obj = await Appartment.create(**appartment_dict)
    return await AppartmentOutSchema.from_tortoise_orm(appartment_obj)

async def delete_appartment(appartment_id: int) -> None:
    deleted_count = await Appartment.filter(id=appartment_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Appartment {appartment_id} not found")
    
async def update_appartment(appartment_id: int, appartment: UpdateAppartment) -> AppartmentOutSchema:
    try:
        await AppartmentOutSchema.from_queryset_single(Appartment.get(id=appartment_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Appartment {appartment_id} not found")
    try:
        await Appartment.filter(id=appartment_id).update(**appartment.dict(exclude_unset=True))
        return await AppartmentOutSchema.from_queryset_single(Appartment.get(id=appartment_id))
    except Exception as e:
        print(e)
        raise