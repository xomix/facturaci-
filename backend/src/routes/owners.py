from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.owners as crud
from src.schemas.owners import OwnerOutSchema, OwnerInSchema, UpdateOwner


router = APIRouter()


@router.get(
    "/owners",
    response_model=List[OwnerOutSchema],
)
async def get_owners():
    return await crud.get_owners()


@router.get(
    "/owners/{owner_id}",
    response_model=OwnerOutSchema
)
async def get_owner(owner_id: int) -> OwnerOutSchema:
    try:
        return await crud.get_owner(owner_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Owner does not exist",
        )

@router.post(
    "/owners", response_model=OwnerOutSchema
)
async def create_owner(
    owner: OwnerInSchema
) -> OwnerOutSchema:
    return await crud.create_owner(owner)

@router.delete(
    "/owners/{owner_id}",
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_owner(
    owner_id: int
):
    await crud.delete_owner(owner_id)

@router.patch(
    "/owners/{owner_id}",
    response_model=OwnerOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_owner(
    owner_id: int,
    owner: UpdateOwner,
) -> OwnerOutSchema:
    return await crud.update_owner(owner_id, owner)