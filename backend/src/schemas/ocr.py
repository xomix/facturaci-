from pydantic import BaseModel, Field
from decimal import Decimal

class ReceiptInfo(BaseModel):
    amount: Decimal = Field(ge=0.01, decimal_places=2)