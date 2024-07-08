from tortoise import fields
from tortoise.models import Model
from enum import Enum
class Owner(Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=50, null=False)
    dni = fields.CharField(max_length=10, null=False)
    address = fields.CharField(max_length=40, null=False)
    email = fields.CharField(max_length=40, null=False)

class Appartment(Model):
    id = fields.IntField(pk=True)
    owner = fields.ForeignKeyField("models.Owner", related_name="appartments")
    alias = fields.CharField(max_length=20)
    address = fields.CharField(max_length=40, null=False)
    zip_code = fields.CharField(max_length=5, null=False)
    city = fields.CharField(max_length=20, null=False)
    province = fields.CharField(max_length=10, null=False)

class Receipt(Model):
    id = fields.IntField(pk=True)
    appartment = fields.ForeignKeyField("models.Appartment", related_name="receipts")
    amount = fields.DecimalField(max_digits=7, decimal_places=2, null=False)
    description = fields.CharField(max_length=40, null=False)
    date = fields.DatetimeField(auto_now_add=True)

class Role(str, Enum):
    ADMIN = "Admin"
    MANAGER = "Manager"
    OWNER = "Owner"
    USER = "User"

class Users(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    role: Role = fields.CharEnumField(Role, default=Role.USER, null=False)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
