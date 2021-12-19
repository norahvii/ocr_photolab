from pdf2image import convert_from_path
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)
import os
import glob

file_pattern = '*.pdf'
file_name_list = []

if '*' in file_pattern:
    file_name_list.extend(glob.glob(file_pattern))

for target in file_name_list:
    images = convert_from_path(target)
    for i, image in enumerate(images):
        fname = target.replace('.pdf',' ') + str(i) + ".png"
        image.save(fname, "PNG")
