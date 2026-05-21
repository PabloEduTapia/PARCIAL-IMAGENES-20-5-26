from PIL import Image


class ImagenIO:
    """Maneja la carga y guardado de imágenes en disco."""

    def cargar(self, ruta):
        """Carga una imagen desde una ruta.

        Args:
            ruta: Ruta del archivo.

        Returns:
            Imagen cargada.
        """
        return Image.open(ruta)
        print("Imagen cargada desde:", ruta)    

    def guardar(self, imagen, ruta):
        """Guarda una imagen.

        Args:
            imagen: Imagen a guardar.
            ruta: Ruta de salida.
        """
        imagen.save(ruta)
        print(f"Imagen guardada en: {ruta}")