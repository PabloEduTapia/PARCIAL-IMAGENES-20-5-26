from PIL import Image
import os

def cargar_imagen(ruta):
    """carga una imagen desde una ruta
    Args:
        ruta: ruta de la imagen
    Returns:
        Imagen cargada.
    """
    return Image.open(ruta)

def guardar_imagen(imagen, carpeta_salida, nombre_archivo):
    """guarda imagen en la carpeta de salida
    Args:
        imagen: imagen procesada.
        carpeta_salida: carpeta donde se guarda el resultado.
        nombre_archivo: nombre del archivo de salida.
    """
    os.makedirs(carpeta_salida, exist_ok=True)
    ruta_salida = os.path.join(carpeta_salida, nombre_archivo)
    imagen.save(ruta_salida)
    print("Imagen guardada en:", ruta_salida)