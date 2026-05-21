def calcular_brillo_promedio(imagen):
    """calcula el brillo promedio
    Args:
        imagen: imagen cargada
    Returns:
        Valor promedio de brillo entre 0 y 255
    """
    gris = imagen.convert("L")
    pixeles = list(gris.getdata())
    promedio = sum(pixeles) / len(pixeles)
    return promedio


def brillo_es_aceptable(promedio):
    """verifica si el brillo es aceptable
    Args:
        promedio: promedio de brillo de la imagen
    Returns:
        true dentro de80 y 170, False otro
    """
    return promedio >= 80 and promedio <= 170