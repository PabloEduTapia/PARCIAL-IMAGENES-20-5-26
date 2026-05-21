import argparse

from procesamiento.archivos import cargar_imagen, guardar_imagen
from procesamiento.analisis import calcular_brillo_promedio, brillo_es_aceptable
from procesamiento.transformaciones import ( convertir_blanco_negro,ajustar_brillo, ajustar_nitidez,aplicar_gaussian_blur)


def mostrar_menu():
    """Menu de opciones."""
    print()
    print("=== MENU DE IMAGENES ===")
    print("1 - Cargar otra imagen")
    print("2 - Convertir a blanco y negro")
    print("3 - Cambiar brillo")
    print("4 - Cambiar nitidez")
    print("5 - Aplicar desenfoque gaussiano")
    print("6 - Salir")


def pedir_valor(mensaje, valor_defecto):
    """Pide un valor numerico. Si no se escribe nada usa el valor por defecto."""
    texto = input(mensaje)
    if texto == "":
        return valor_defecto
    return float(texto)

def cargar_desde_consola():
    """Pide ruta para cargar la iamgen"""
    ruta = input("Ingrese ruta de la imagen. Defecto usa input/ciudad.png: ")
    if ruta == "":
        ruta = "input/ciudad.png"
    imagen = cargar_imagen(ruta)
    print("Imagen cargada:", ruta)    
    return imagen, ruta

def main():
    """Entrada principal del programa."""    
    parser = argparse.ArgumentParser(description="Procesamiento de imagenes")
    parser.add_argument(
        "--ruta",
        default="input/ciudad.png",
        help="Rutaimagen. DEfault usa input/ciudad.png"
    )

    parser.add_argument(
        "--salida",
        default="output",
        help="Carpeta guardan las imagenes procesadas"
    )

    args = parser.parse_args()
    # Cargo la imagen una sola vez.
    imagen = cargar_imagen(args.ruta)

    print("Imagen cargada:", args.ruta)
    print("Tamaño:", imagen.size)
    print("Modo:", imagen.mode)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            # permite cambiar la imagen
            imagen, ruta_actual = cargar_desde_consola()
        if opcion == "2":
            # cambia la imagen a b y n
            resultado = convertir_blanco_negro(imagen)
            guardar_imagen(resultado, args.salida, "output_blanco_negro.png")
        elif opcion == "3":
            # primero medimos el brillo origial
            brillo_inicial = calcular_brillo_promedio(imagen)
            print("Brillo inicial:", brillo_inicial)
            # si es 1.0 deja igual mayor a 1 aumenta el brillo.
            factor = pedir_valor("Factor de brillo. Enter usa 1.3: ", 1.3)
            resultado = ajustar_brillo(imagen, factor)

            # se vuelve a medir el brillo para ver si mejora
            brillo_final = calcular_brillo_promedio(resultado)
            print("Brillo final:", brillo_final)
            if brillo_es_aceptable(brillo_final):
                print("El brillo esta en el rango esperado.")
            else:
                print("El brillo quedo fuera del rango esperado.")

            guardar_imagen(resultado, args.salida, "output_brillo.png")

        elif opcion == "4":
            # valor 1.0 deja la imagen igual
            # mayor aumenta la nitidez
            factor = pedir_valor("Valor de nitidez. Enter usa 2.0(defecto): ", 2.0)
            resultado = ajustar_nitidez(imagen, factor)
            guardar_imagen(resultado, args.salida, "output_nitidez.png")

        elif opcion == "5":
            # a mayor radio mas desenfoque.
            radio = pedir_valor("Valor del desenfoque. Enter usa 2(defecto): ", 2)
            resultado = aplicar_gaussian_blur(imagen, radio)
            guardar_imagen(resultado, args.salida, "output_gaussian_blur.png")

        elif opcion == "6":
            print("Fin :).")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    main()