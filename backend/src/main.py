from fastapi import FastAPI, UploadFile
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

from src.routes import appartments, owners, ocr, receipts

app = FastAPI()

app.include_router(appartments.router)
app.include_router(owners.router)
app.include_router(ocr.router)
app.include_router(receipts.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "Hello, World!"