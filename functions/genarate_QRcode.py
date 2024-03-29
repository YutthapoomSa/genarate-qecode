import os
import openpyxl
import qrcode
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

def create_qrcode():
    root_path = "./config/"

    xlsx_path = os.path.join(root_path, 'number.xlsx')
    df = pd.read_excel(xlsx_path)

    output_folder = os.path.join(root_path, 'qrcodes')
    os.makedirs(output_folder, exist_ok=True)

    for value in df['number']:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(str(value))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(os.path.join(output_folder, f"{value}.png"))

        img_path = os.path.join(output_folder, f"{value}.png")
        img = Image.open(img_path)
        qr_number = str(value)

        # Calculate the center of the image
        center_x, center_y = img.width // 2, img.height // 2

        # Create a drawing object
        draw = ImageDraw.Draw(img)

        # Determine the position to place the number (centered)
        text_width, text_height = draw.textsize(qr_number)
        text_x = center_x - (text_width // 2)
        text_y = center_y - (text_height // 2)

        # Draw the text on the image with the updated font size
        font_size = 18
        font = ImageFont.truetype(os.path.join(root_path, "font/Arial.ttf"), font_size)
        draw.text((text_x - 10, text_y + 110), qr_number, fill="black", font=font)

        img.save(img_path)

    print("QR codes with numbers have been generated.")
