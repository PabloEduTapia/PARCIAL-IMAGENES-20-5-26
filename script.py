"""01 - Cargar y describir una imagen con Pillow."""
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import cv2
import numpy as np

img = Image.open("input/ciudad.png")
print(img.size, img.mode)

arr = np.asarray(img)
print(arr.shape, arr.dtype)
print("pixel (0,0) =", arr[0, 0])

gris      = ImageOps.grayscale(img)
gris.save("output/output_gris.png")


gris_analisis = img.convert("L")
gris_analisis.save("output/output_gris_analisis.png")
pixeles = list(gris_analisis.getdata())
promedio = sum(pixeles) / len(pixeles)
print("Promedio de intensidad:", promedio)


"""0 a 80     → imagen oscura
80 a 170   → brillo medio
170 a 255  → imagen clara"""

"""ruido = diferencia promedio entre imagen gris original y una versión suavizada"""
"""contraste = desviación estándar de los píxeles en gris"""


contraste = ImageEnhance.Contrast(img).enhance(1.6)
contraste.save("output/output_contraste.png")


nitidez = ImageEnhance.Sharpness(img).enhance(2.0)
nitidez.save("output/output_nitidez.png")

suavizado = img.filter(ImageFilter.SMOOTH)
suavizado.save("output/output_suavizado.png")

detalles = img.filter(ImageFilter.DETAIL)
detalles.save("output/output_detail.png")

GaussianBlur = img.filter(ImageFilter.GaussianBlur(radius=2))
GaussianBlur.save("output/output_gaussian_blur.png")


