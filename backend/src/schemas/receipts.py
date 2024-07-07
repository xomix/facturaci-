from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Receipt
from datetime import datetime

ReceiptInSchema = pydantic_model_creator(
    Receipt, name="ReceiptIn", exclude_readonly=True)
ReceiptOutSchema = pydantic_model_creator(
    Receipt, name="Receipt")

class UpdateReceipt(BaseModel):
    amount: Optional[Decimal] = Field(ge=0.01, decimal_places=2, default=None)
    description: Optional[str] = Field(default=None)
    date: Optional[datetime] = Field(default=None)