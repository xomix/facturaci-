from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.appartments as crud
from src.schemas.appartments import AppartmentOutSchema, AppartmentInSchema, UpdateAppartment


router = APIRouter()


@router.get(
    "/appartments",
    response_model=List[AppartmentOutSchema],
)
async def get_appartments():
    return await crud.get_appartments()


@router.get(
    "/appartments/{appartment_id}",
    response_model=AppartmentOutSchema
)
async def get_appartment(appartment_id: int) -> AppartmentOutSchema:
    try:
        return await crud.get_appartment(appartment_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Appartment does not exist",
        )

@router.post(
    "/appartments", response_model=AppartmentOutSchema
)
async def create_appartment(
    appartment: AppartmentInSchema
) -> AppartmentOutSchema:
    return await crud.create_appartment(appartment)

@router.delete(
    "/appartments/{appartment_id}",
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_appartment(
    appartment_id: int
):
    await crud.delete_appartment(appartment_id)

@router.patch(
    "/appartments/{appartment_id}",
    response_model=AppartmentOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_appartment(
    appartment_id: int,
    appartment: UpdateAppartment,
) -> AppartmentOutSchema:
    return await crud.update_appartment(appartment_id, appartment)