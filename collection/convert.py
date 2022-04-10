import glob
import os

import pytesseract
from pdf2image import convert_from_path
from pdf2image.exceptions import (PDFInfoNotInstalledError, PDFPageCountError,
                                  PDFSyntaxError)
from PIL import Image

file_pattern = '*.pdf'
file_name_list = []

if '*' in file_pattern:
    file_name_list.extend(glob.glob(file_pattern))

for target in file_name_list:
    images = convert_from_path(target)
    for i, image in enumerate(images):
        fname = target.replace('.pdf',' ') + str(i) + ".png"
        image.save(fname, "PNG")

png_pattern = '*.png'
png_name_list = []

if '*' in png_pattern:
    png_name_list.extend(glob.glob(png_pattern))

with open("out.txt", "w") as external_file:
        for target in png_name_list:
                print(pytesseract.image_to_string(Image.open(target)), file=external_file)
		#os.remote(target)
