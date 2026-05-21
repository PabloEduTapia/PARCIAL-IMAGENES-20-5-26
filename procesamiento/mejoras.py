from PIL import ImageEnhance


class MejoradorImagen:
    """aplica mejoras visuales a imagen"""
    def ajustar_brillo(self, imagen, factor):
        """Ajusta brillo a imagen
        Args:
            imagen: imagen original
            factor: Factor de brillo
        Returns:
            imagen con brillo cambiado"""
        return ImageEnhance.Brightness(imagen).enhance(factor)