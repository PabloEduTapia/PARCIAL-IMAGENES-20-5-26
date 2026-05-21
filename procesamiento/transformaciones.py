from PIL import ImageEnhance, ImageFilter


def convertir_blanco_negro(imagen):
    """convierte una imagen a blanco y negro
    Args:
        imagen: imagen original
    Returns:
        Imagen en blanco y negro
    """
    return imagen.convert("L")


def ajustar_brillo(imagen, factor):
    """Ajusta el brillo de una imagen
    Args:
        imagen: imagen original.
        factor: valor de brillo
    Returns:
        Imagen con brillo cambiado
    """
    return ImageEnhance.Brightness(imagen).enhance(factor)


def ajustar_nitidez(imagen, factor):
    """Cambia la nitidez de una imagen
    Args:
        imagen: imagen original
        factor: valor de nitidez
    Returns:
        Imagen con nitidez cambiada
    """
    return ImageEnhance.Sharpness(imagen).enhance(factor)


def aplicar_gaussian_blur(imagen, radio):
    """Aplica desenfoque gaussiano a una imagen
    Args:
        imagen: imagen original
        radio: valor del desenfoques
    Returns:
        Imagen desenfocada
    """
    return imagen.filter(ImageFilter.GaussianBlur(radius=radio))