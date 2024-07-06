from pydantic import BaseModel, Field
from typing import Optional
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Appartment

AppartmentInSchema = pydantic_model_creator(
    Appartment, name="AppartmentIn", exclude_readonly=True)
AppartmentOutSchema = pydantic_model_creator(
    Appartment, name="Appartment")

class UpdateAppartment(BaseModel):
    address : Optional[str] = Field(default=None)
    zip_code: Optional[str] = Field(default=None)
    city    : Optional[str] = Field(default=None)
    province: Optional[str] = Field(default=None)
    alias   : Optional[str] = Field(default=None)
