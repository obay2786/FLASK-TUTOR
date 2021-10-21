from PIL import Image, ImageOps
import base64
from io import BytesIO
import os 
import secrets


def saveImages(photo):
    randomHex = secrets.token_hex(8)
    _, file_ex = os.path.splitext(photo.filename)
    pictureFn = randomHex + file_ex
    picturePath = os.path.join(os.getcwd(),'upload/staff',pictureFn)
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)
    output_size = (700, 700)
    img.thumbnail(output_size)
    img.save(picturePath)
    return pictureFn

