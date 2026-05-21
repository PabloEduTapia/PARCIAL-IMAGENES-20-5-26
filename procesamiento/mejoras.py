from PIL import ImageEnhance


class MejoradorImagen:
    """Aplica mejoras visuales sobre la imagen."""

    def ajustar_brillo(self, imagen, factor):
        """Ajusta el brillo de la imagen.

        Args:
            imagen: Imagen original.
            factor: Factor de brillo. 1.0 mantiene igual, mayor aumenta, menor reduce.

        Returns:
            Imagen con brillo ajustado.
        """
        return ImageEnhance.Brightness(imagen).enhance(factor)