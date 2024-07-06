from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.post("/receipt/")
async def create_upload_receipt(file: UploadFile):
    print(file.filename, file.size)
