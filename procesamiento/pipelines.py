from procesamiento.analisis import AnalizadorImagen
from procesamiento.mejoras import MejoradorImagen


class PipelineMejoraImagen:
    """Ejecuta el flujo de análisis y mejora de una imagen."""

    def __init__(self):       
        self.analizador = AnalizadorImagen()
        self.mejorador = MejoradorImagen()

    def decidir_factor_brillo(self, promedio):
        """Decide el factor de brillo según el promedio de intensidad.

        Args:
            promedio: Brillo promedio entre 0 y 255.

        Returns:
            Factor numérico para aplicar con ImageEnhance.Brightness.
        """
        if promedio < 60:
            return 1.5
        elif promedio < 80:
            return 1.3
        elif promedio <= 170:
            return 1.0
        elif promedio <= 210:
            return 0.9
        else:
            return 0.75

    def mejorar_brillo(self, imagen):
        """Analiza y mejora el brillo de una imagen.

        Args:
            imagen: Imagen original.

        Returns:
            Imagen mejorada, promedio original y factor aplicado.
        """
        promedio = self.analizador.calcular_brillo_promedio(imagen)
        promedio_inicial = self.analizador.calcular_brillo_promedio(imagen)
        factor = self.decidir_factor_brillo(promedio)
        imagen_mejorada = self.mejorador.ajustar_brillo(imagen, factor)
        promedio_final = self.analizador.calcular_brillo_promedio(imagen_mejorada)        
        brillo_aceptable = 80 <= promedio_final <= 170
        print("Promedio de brillo:", promedio)
        print("Factor aplicado:", factor)  
        print("Brillo clasificado como:", self.analizador.clasificar_brillo(promedio)) 
        return imagen_mejorada, promedio_inicial, promedio_final, factor, brillo_aceptable