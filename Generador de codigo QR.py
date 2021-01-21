# Generando codigos QR
import pyqrcode
from pyqrcode import QRCode
# string que representa el codigo QR
s = 'https://youtu.be/gGelEHegLac'
# Generador de codigo QR
url = pyqrcode.create(s)
# Creando y guardando el archivo png con el nombre 'myqr.png'
url.svg("sovalor.svg", scale= 8)