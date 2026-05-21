from procesamiento.imagenes import ImagenIO
from procesamiento.pipelines import PipelineMejoraImagen


io = ImagenIO()
pipeline = PipelineMejoraImagen()

imagen = io.cargar("input/ciudad.png")

imagen_mejorada, promedio, factor = pipeline.mejorar_brillo(imagen)

print("Promedio de brillo:", promedio)
print("Factor aplicado:", factor)

io.guardar(imagen_mejorada, "output/output_brillo_mejorado.png")