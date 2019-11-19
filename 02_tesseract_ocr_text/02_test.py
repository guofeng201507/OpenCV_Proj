from PIL import Image
import pytesseract
import os

from pathlib import Path

PATH = Path.cwd()

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# path = "text-image.png"
# path_cn = "text-image-cn.png"
#
# text_en = pytesseract.image_to_string(Image.open(path))
# print(text_en)
#
# text_cn = pytesseract.image_to_string(Image.open(path_cn), lang='chi_sim')
# print(text_cn)

code_path = os.path.join(PATH, 'code_photo/IMG_20191119_215129.jpg')

text_en = pytesseract.image_to_string(Image.open(code_path))
print(text_en)
