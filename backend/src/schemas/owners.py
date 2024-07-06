from pydantic import BaseModel, Field
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Owner

OwnerInSchema = pydantic_model_creator(
    Owner, name="OwnerIn", exclude_readonly=True)
OwnerOutSchema = pydantic_model_creator(
    Owner, name="Owner")

class UpdateOwner(BaseModel):
    dni      : Optional[str] = Field(default=None)
    full_name: Optional[str] = Field(default=None)
    address  : Optional[str] = Field(default=None)
    email    : Optional[str] = Field(default=None)