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
    opcion=int(input("Ingrese su opcion: "))

    if opcion==1:
        for i in mostrar_lista_peliculas(DIRECCION):
            print(str(i[0])+")",i[1])
    elif opcion == 2:
        num_preguntas = int(input("Ingresa el número de preguntas para la trivia (entre 3 y 10): "))
        if num_preguntas < 3 or num_preguntas > 10:
            print("El número de preguntas debe estar entre 3 y 10.")
        else:
            trivia = generar_trivia(DIRECCION, num_preguntas)
            for pregunta in trivia:
                opciones = [pregunta]
                while len(opciones) < 3:
                    opcion = random.choice(DIRECCION)
                    if opcion != pregunta:
                        opciones.append(opcion)
                mostrar_y_validar_opciones(pregunta, opciones)
                opciones_seleccionadas.append(pregunta)  
    elif opcion == 3:
            pass
    elif opcion == 4:
        opciones_seleccionadas = []
        print("Historial de opciones borrado.")
    elif opcion == 5:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")