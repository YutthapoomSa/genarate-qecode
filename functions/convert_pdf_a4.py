import os
import cv2
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import qrcode
from PIL import Image

input_folder = root_path+'qrcodes2'
output_folder = root_path
output_pdf_filename = 'ร้อย.พล.สร.รพ.ค่ายวชิราวุธ.pdf'

# Create a PDF file and add a grid of images
pdf_path = os.path.join(output_folder, output_pdf_filename)

c = canvas.Canvas(pdf_path, pagesize=A4)

# Determine the number of rows and columns in the grid
num_rows = 6
num_columns = 6

# Calculate the size of each square cell
cell_size = min(A4[0] / num_columns, A4[1] / num_rows)

image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
image_files = image_files[:min(len(image_files), num_rows * num_columns)]

# Create QR codes for images and add them to the PDF
for row in range(num_rows):
    for col in range(num_columns):
        if not image_files:
            break

        image_file = image_files.pop(0)
        image_path = os.path.join(input_folder, image_file)

        with Image.open(image_path) as img:
            img.thumbnail((cell_size, cell_size))
            width, height = img.size
            x = col * cell_size + (cell_size - width) / 2
            y = A4[1] - (row + 1) * cell_size + (cell_size - height) / 2
            c.drawImage(image_path, x, y, width, height)

c.showPage()
c.save()