class AnalizadorImagen:
    """Analiza características básicas de la imagen."""

    def calcular_brillo_promedio(self, imagen):
        """Calcula el brillo promedio de la imagen.

        Args:
            imagen: Imagen entrada.

        Returns:
            Promedio de intensidad entre 0 y 255.
        """
        gris = imagen.convert("L")
        pixeles = list(gris.getdata())
        promedio = sum(pixeles) / len(pixeles)
        print("Promedio de intensidad:", promedio)
        return promedio

    def clasificar_brillo(self, promedio):
        """Clasifica el brillo promedio de una imagen.

        Args:
            promedio: Valor promedio de intensidad entre 0 y 255.

        Returns:
            Texto descriptivo: 'oscura', 'media' o 'clara'.
        """
        if promedio < 80:
            return "oscura"
        elif promedio <= 170:
            return "media"
        else:
            return "clara"
        print("Brillo clasificado como:", self.clasificar_brillo(promedio)) 