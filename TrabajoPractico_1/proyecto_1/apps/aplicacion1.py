# Aplicación secundaria
from modules.funciones import mostrar_lista_peliculas, trivia, guardar_opciones, mostrar_opciones_seleccionadas, borrar_opciones

import random

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
DIRECCION1=RUTA + "registro_de_opciones_seleccionadas.txt"
lista_opciones=[]
opcion=int(input("Ingrese una opcion: "))
guardar_opciones(opcion)
with open(DIRECCION,"r",encoding="utf-8") as archi: # utf-8 reconoce caracteres especiales en la Lista
        lista1=archi.readlines()
        frases_y_pelis = [(linea.strip().split(';')[0], linea.strip().split(';')[1]) for linea in lista1]  #strip suprime blancos y split va a separar hasta el ;
while opcion!=5:
    if opcion == 1:
        for i in mostrar_lista_peliculas (DIRECCION):
            print(str(i[0])+")",i[1])
    elif opcion==2:
        x=int(input("Elija la cantidad de veces que quiere jugar la trivia, debe ser entre 3 y 10: "))
        if x >= 3 and x<=10:
            for i in range (0,x):
                lista1=trivia(frases_y_pelis)
                print ("Adivine a que película pertenece la siguiente frase:", lista1[0])
                print("Las opciones para elegir son: ")
                for i,pelicula in enumerate(lista1[2]):
                    print(i+1,pelicula)
                opcion=int (input("Elija la opción correcta, ingresando 1, 2 o 3 : "))
                if opcion-1==lista1[2].index(lista1[1]):
                    print("¡¡Felicitaciones,la opción elegida es la correcta!!!")
                elif opcion-1!=lista1[2].index(lista1[1]):
                    if opcion!=1 and opcion!=2 and opcion!=3:
                     print("El número ingresado no es una opción posible")
                    else:
                        print("La opción es incorrecta :( ")
            print("\n ¡ Gracias por participar!!!")
        else:
            print("Debe elegir un valor entre 3 y 10")
    elif opcion==3:
        opciones_seleccionadas=mostrar_opciones_seleccionadas (DIRECCION1)
        print("Las opciones seleccionadas previamente son: ")
        print(opciones_seleccionadas +"\n")
    elif opcion==4:
        borrar_opciones (DIRECCION1)
        print("El historial se eliminó correctamente")
    elif opcion>5:
        print("La opción elegida no es correcta, vuelva a intentarlo.")
    opcion=int (input("Ingrese otra opción: "))
    guardar_opciones (opcion)
if opcion==5:
    print("Gracias por utilizar el programa.")