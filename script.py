"""01 - Cargar y describir una imagen con Pillow.
Pruebas

archivo borrador.
fuimos probando todo junto antes de separar EL CODIGO
"""

from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import cv2
import numpy as np
import os


# carpeta output 
os.makedirs("output", exist_ok=True)


# carga la imagen base
img = Image.open("input/ciudad.png")

print("datos de la imagen")
print(img.size, img.mode)


# array de pixeles
arr = np.asarray(img)

print(arr.shape, arr.dtype)
print("pixel (0,0) =", arr[0, 0])


# pasar a blanco y negro / gris
gris = ImageOps.grayscale(img)
gris.save("output/output_gris.png")


# analisis de brillo
gris_analisis = img.convert("L")
gris_analisis.save("output/output_gris_analisis.png")

pixeles = list(gris_analisis.getdata())
promedio = sum(pixeles) / len(pixeles)

print("Promedio:", promedio)


"""
Rangos sugeridos

0 a 80     -> imagen oscura
80 a 170   -> brillo medio o aceptable
170 a 255  -> imagen clara
"""


#  mejorar brillo segun promedio
if promedio < 80:
    print("oscura")
    factor_brillo = 1.4

elif promedio > 170:
    print("clara")
    factor_brillo = 0.8

else:
    print("medio")
    factor_brillo = 1.0


brillo = ImageEnhance.Brightness(img).enhance(factor_brillo)
brillo.save("output/output_brillo.png")


# 
gris_despues = brillo.convert("L")
pixeles_despues = list(gris_despues.getdata())
promedio_despues = sum(pixeles_despues) / len(pixeles_despues)

print("Promedio despues:", promedio_despues)


if promedio_despues >= 80 and promedio_despues <= 170:
    print("el brillo esta OK")
else:
    print("mal brillo despues de la mejora")


"""
ruido = diferencia promedio entre imagen gris original y una version suavizada
contraste = desviacion estandar de los pixeles en gris
"""


# analisis de contraste
arr_gris = np.asarray(gris_analisis)
valor_contraste = np.std(arr_gris)

print("Contraste:", valor_contraste)


# mejorar contraste
if valor_contraste < 35:
    print("bajo contraste")
    factor_contraste = 1.6

elif valor_contraste < 70:
    print("contraste medio")
    factor_contraste = 1.3

else:
    print("contraste alto")
    factor_contraste = 1.0


contraste = ImageEnhance.Contrast(img).enhance(factor_contraste)
contraste.save("output/output_contraste.png")


# nitidez
nitidez = ImageEnhance.Sharpness(img).enhance(2.0)
nitidez.save("output/output_nitidez.png")


#suavizado
suavizado = img.filter(ImageFilter.SMOOTH)
suavizado.save("output/output_suavizado.png")


# filtro detalle
detalles = img.filter(ImageFilter.DETAIL)
detalles.save("output/output_detail.png")


# desenfoque gaussiano
GaussianBlur = img.filter(ImageFilter.GaussianBlur(radius=2))
GaussianBlur.save("output/output_gaussian_blur.png")


#  medir ruido 
gris_suave = gris_analisis.filter(ImageFilter.GaussianBlur(radius=2))
arr_original = np.asarray(gris_analisis, dtype=np.int16)
arr_suavizado = np.asarray(gris_suave, dtype=np.int16)
diferencia = np.abs(arr_original - arr_suavizado)
ruido = np.mean(diferencia)
print("Ruido:", ruido)

if ruido < 5:
    print("bajo ruido")

elif ruido < 15:
    print("medio ruido")

else:
    print(" alto ruido")










    