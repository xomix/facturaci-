from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist
from src.database.models import Receipt
from src.schemas.receipts import ReceiptOutSchema, ReceiptInSchema, UpdateReceipt


async def get_receipts():
    return await ReceiptOutSchema.from_queryset(Receipt.all())

async def get_receipt(receipt_id: int) -> ReceiptOutSchema:
    return await ReceiptOutSchema.from_queryset_single(Receipt.get(id=receipt_id))

async def create_receipt(receipt: ReceiptInSchema) -> ReceiptOutSchema:
    receipt_dict = receipt.model_dump(exclude_unset=True)
    receipt_obj = await Receipt.create(**receipt_dict)
    return await ReceiptOutSchema.from_tortoise_orm(receipt_obj)

async def delete_receipt(receipt_id: int) -> None:
    deleted_count = await Receipt.filter(id=receipt_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Receipt {receipt_id} not found")
    
async def update_receipt(receipt_id: int, receipt: UpdateReceipt) -> ReceiptOutSchema:
    try:
        await ReceiptOutSchema.from_queryset_single(Receipt.get(id=receipt_id))
    except DoesNotExist as e:
        raise HTTPException(status_code=404, detail=f"Receipt {receipt_id} not found") from e

    await Receipt.filter(id=receipt_id).update(**receipt.dict(exclude_unset=True))
    return await ReceiptOutSchema.from_queryset_single(Receipt.get(id=receipt_id))