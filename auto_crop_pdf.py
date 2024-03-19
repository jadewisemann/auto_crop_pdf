from PIL import Image
import os
from PyPDF2 import PdfMerger
merger = PdfMerger()

# Get Input
point_1 = ""
point_2 = ""
original_path = ""

# Parse Input
crop_area  = (point_1[0], point_1[1], point_2[0], point_2[1])
cropped_img_path = f"{original_path}[cropped]"
pdf_pages_path = f"{original_path}[pdf]"
output_pdf_name = f"{list(original_path.split('/'))[-1]}.pdf"

# Make Folders
if not os.path.exists(cropped_img_path):
    os.makedirs(cropped_img_path)
if not os.path.exists(pdf_pages_path):
    os.makedirs(pdf_pages_path)

# Variable
current_index = 0

# Get Every Target files
image_files = [file for file in os.listdir(original_path) if file.lower().endswith(('.jpg', '.png'))]  
total_images = len(image_files) 

# Looping
for filename in image_files:
    current_index += 1
    image_path = os.path.join(original_path, filename)
    img = Image.open(image_path)
    # crop, img
    cropped_img = img.crop(crop_area)
    # save, img
    output_filename = f"{str(current_index).zfill(3)}.pdf"
    output_path = os.path.join(pdf_pages_path, output_filename)
    # convert, img to pdf page
    cropped_img.convert('RGB').save(output_path)  
    # print, progress
    print(f"progress: {current_index}/{total_images} ({(current_index/total_images)*100:.2f}%)")

# Merge, pdf pages to single Pdf
for pdf in [os.path.join(pdf_pages_path, file) for file in os.listdir(pdf_pages_path) if file.endswith('.pdf')]:
    merger.append(pdf)
    
merger.write(os.path.join(os.path.dirname(original_path), output_pdf_name))
merger.close()

print(f"PDF Merge Success.")
