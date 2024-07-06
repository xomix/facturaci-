from tortoise import fields
from tortoise.models import Model

class Owner(Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=50, null=False)
    dni = fields.CharField(max_length=10, null=False)
    address = fields.CharField(max_length=40, null=False)

class Appartment(Model):
    id = fields.IntField(pk=True)
    #owner = fields.ForeignKeyField("models.Owners", related_name="id")
    alias = fields.CharField(max_length=20)
    owner = fields.CharField(max_length=50, null=False)
    address = fields.CharField(max_length=40, null=False)
    zip_code = fields.CharField(max_length=5, null=False)
    city = fields.CharField(max_length=20, null=False)
    province = fields.CharField(max_length=10, null=False)
