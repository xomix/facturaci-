from collections import defaultdict
from fastapi import UploadFile, HTTPException
from src.schemas.ocr import ReceiptInfo
from pytesseract import image_to_data, Output
from pdf2image import convert_from_bytes
from typing import Any
from pydantic import BaseModel
import re
from io import BytesIO
from PIL import Image
from decimal import Decimal

MAX_FILE_SIZE = 3*1024*1024

RE_TOTAL = re.compile(r'(?<!sub)total', re.IGNORECASE)
RE_AMOUNT = re.compile(r'(\d+)[,.](\d+)')

class TesseractEntry(BaseModel):
    level: int
    page_num: int
    block_num: int
    line_num: int
    word_num: int
    left: int
    top: int
    width: int
    height: int
    conf: float
    text: str

def get_list_entries(data: dict[str, list[Any]]) -> list[TesseractEntry]:
    entries = []
    for i in range(len(data['level'])):
         entry = {k: data[k][i] for k in data.keys()}
         entries.append(TesseractEntry(**entry))
         
    return entries

def filter_list_entries(entries: list[TesseractEntry]) -> list[TesseractEntry]:
     return [entry for entry in entries if entry.conf > 0]

def group_by_line(entries: list[TesseractEntry]) -> list[str]:
    line_dict = defaultdict(list)
    for entry in entries:
         line_dict[(entry.block_num, entry.line_num)].append(entry.text)
    lines = [ ''.join(v) for _, v in sorted(line_dict.items()) ]

    return lines

async def process_receipt_image(file: UploadFile) -> ReceiptInfo:
    # TODO Read in chunks
    if file.size > MAX_FILE_SIZE:
        raise HTTPException(status_code=418, detail="File size is too large")
    print(file.content_type)
    if file.content_type == 'application/pdf':
        image = convert_from_bytes(await file.read())[0]
    else:
        image = Image.open(BytesIO(await file.read()))
    try:
        #text = image_to_string(pages[0], lang="spa+fr+ca", timeout=2)
        data: dict[str, list[Any]] = image_to_data(image, lang="spa+fr+ca", output_type=Output.DICT, timeout=2)
    except RuntimeError:
            raise HTTPException(status_code=418, detail="File processing stopped: took too long")
    entries = group_by_line(filter_list_entries(get_list_entries(data)))

    # Try to find the "TOTAL" amount of the receipt
    amount = 0.01
    for line in entries:
        total_line = RE_TOTAL.search(line)
        if not total_line :
            continue
        amount_match = RE_AMOUNT.search(line)
        print(line)

        if amount_match:
            amount = Decimal(f"{amount_match.group(1)}.{amount_match.group(2)}")

    return ReceiptInfo(amount=amount)