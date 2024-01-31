import os
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse
from typing import List
from functions.create_file_xlsx import create_file
from functions.genarate_QRcode import create_qrcode
from functions.convert_pdf_a4 import convert_pdf
from pydantic import BaseModel


courses_routes_qrcode = APIRouter()

class Item(BaseModel):
    data: List[str]

@courses_routes_qrcode.post("/create")
async def generate_qrcode(item: Item):
    try:
        data = item.data
        if data:
            file_xlsx = create_file(data)
            if os.path.isfile(file_xlsx):
                create_qrcode()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    finally:
        file_pdf = convert_pdf()
        response = FileResponse(
            file_pdf,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=file.pdf"}
        )
        return response