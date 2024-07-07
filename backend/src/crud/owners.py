from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist
from src.database.models import Owner
from src.schemas.owners import OwnerOutSchema, OwnerInSchema, UpdateOwner


async def get_owners():
    return await OwnerOutSchema.from_queryset(Owner.all())


async def get_owner(owner_id: int) -> OwnerOutSchema:
    return await OwnerOutSchema.from_queryset_single(Owner.get(id=owner_id))

async def create_owner(owner: OwnerInSchema) -> OwnerOutSchema:
    owner_dict = owner.model_dump(exclude_unset=True)
    owner_obj = await Owner.create(**owner_dict)
    return await OwnerOutSchema.from_tortoise_orm(owner_obj)

async def delete_owner(owner_id: int) -> None:
    deleted_count = await Owner.filter(id=owner_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Owner {owner_id} not found")
    
async def update_owner(owner_id: int, owner: UpdateOwner) -> OwnerOutSchema:
    try:
        await OwnerOutSchema.from_queryset_single(Owner.get(id=owner_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Owner {owner_id} not found")
    try:
        await Owner.filter(id=owner_id).update(**owner.model_dump(exclude_unset=True))
        return await OwnerOutSchema.from_queryset_single(Owner.get(id=owner_id))
    except Exception as e:
        print(e)
        raise