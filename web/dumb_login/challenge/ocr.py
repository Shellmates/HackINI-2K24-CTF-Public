from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def ocr(image_stream):
    image = Image.open(image_stream)
    text = pytesseract.image_to_string(image)
    return text
