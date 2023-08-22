# Aplicación secundaria
from modules.modulo1 import mostrar_lista_peliculas
from modules.modulo1 import generar_trivia
from modules.modulo1 import mostrar_y_validar_opciones
import random




    
opciones_seleccionadas = []

print("""
        #######################################
        #  Películas: Preguntas y respuestas  #
        #######################################
        Elige una opción
        1 - Mostrar lista de películas.
        2 - ¡Trivia de pelí1cula!
        3 - Mostrar secuencia de opciones seleccionadas previamente.
        4 - Borrar historial de opciones.
        5 - Salir
        """
)
RUTA="./data/"
DIRECCION=RUTA + "frases_de_peliculas.txt"
while True:
    opcion=input("Ingrese su opcion: ")

    lis, pelis = mostrar_lista_peliculas(DIRECCION)

    if opcion=='1':
        for i, p in enumerate(sorted(pelis)):
            print(i+1, p)
    elif opcion == '2':
        num_preguntas = int(input("Ingresa el número de preguntas para la trivia (entre 3 y 10): "))
        if num_preguntas < 3 or num_preguntas > 10:
            print("El número de preguntas debe estar entre 3 y 10.")
        else:
            trivia = generar_trivia(lis, num_preguntas)
            for lis in trivia:
                opciones = pelis
                while len(opciones) < 3:
                    opcion = random.choice(opcion)
                    if opcion != lis:
                        opciones.append(opcion)
                mostrar_y_validar_opciones(lis, opciones)
                opciones_seleccionadas.append(lis) 
            while True:
                try:
                    seleccion = int(input("Selecciona la opción correcta (1/2/3): "))
                    if seleccion < 1 or seleccion > 3:
                        print("Por favor, selecciona una opción válida.")
                    else:
                        if seleccion == respuesta_correcta + 1:
                            print("¡Correcto! ¡Felicitaciones!\n")
                        else:
                            print(f"Incorrecto. La respuesta correcta era: {respuesta_correcta + 1} - {lista}\n")
                        break
                except ValueError:
                    print("Por favor, introduce un número válido.")
            
    elif opcion == '3':
            pass
    elif opcion == '4':
        opciones_seleccionadas = []
        print("Historial de opciones borrado.")
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")