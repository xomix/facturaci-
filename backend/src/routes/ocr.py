from fastapi import APIRouter, UploadFile

import src.ocr as ocr
from src.schemas.ocr import ReceiptInfo



router = APIRouter()


@router.post(
    "/ocr",
    response_model=ReceiptInfo,
)
async def do_ocr(file: UploadFile):
    return await ocr.process_receipt_image(file)