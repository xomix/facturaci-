from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.receipts as crud
from src.schemas.receipts import ReceiptOutSchema, ReceiptInSchema, UpdateReceipt


router = APIRouter()


@router.get(
    "/receipts",
    response_model=List[ReceiptOutSchema],
)
async def get_receipts():
    return await crud.get_receipts()


@router.get(
    "/receipts/{receipt_id}",
    response_model=ReceiptOutSchema
)
async def get_receipt(receipt_id: int) -> ReceiptOutSchema:
    try:
        return await crud.get_receipt(receipt_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Receipt does not exist",
        )

@router.post(
    "/receipts", response_model=ReceiptOutSchema
)
async def create_receipt(
    receipt: ReceiptInSchema
) -> ReceiptOutSchema:
    return await crud.create_receipt(receipt)

@router.delete(
    "/receipts/{receipt_id}",
    responses={404: {"model": HTTPNotFoundError}},
)
async def delete_receipt(
    receipt_id: int
):
    await crud.delete_receipt(receipt_id)

@router.patch(
    "/receipts/{receipt_id}",
    response_model=ReceiptOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_receipt(
    receipt_id: int,
    receipt: UpdateReceipt,
) -> ReceiptOutSchema:
    return await crud.update_receipt(receipt_id, receipt)