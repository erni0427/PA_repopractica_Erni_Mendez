# módulo para organizar funciones o clases utilizadas en nuestro proyecto
import random
import datetime


def mostrar_lista_peliculas(archivo_peliculas):
    """Función que lee el archivo con las frases de las peliculas y las muestra en una lista de tuplas
    """
    lista=[]
    lista_sin_repe=[]
    with open(archivo_peliculas, "r", encoding="utf-8") as archi: #el encoding se utiliza para caracteres especiales
        for linea in archi:
            frase, pelicula = linea.rstrip("\n").split(';')
            lista.append(pelicula)
    lista_sin_repe=set(lista)
    return [(i+1, elemento) for i,elemento in enumerate (sorted(lista_sin_repe))] #elemento no es variable

def trivia (archivo_peliculas):
    """Función que lee el archivo con las frases de las peliculas y extrae 3 películas y 1 frase al azar"""
    with open(archivo_peliculas,"r",encoding="utf-8") as archi: # utf-8 reconoce caracteres especiales en la Lista
        lista1=archi.readlines()
        frases_y_pelis = [(linea.strip().split(';')[0], linea.strip().split(';')[1]) for linea in lista1]  #strip suprime blancos y split va a separar hasta el ;
        op_ganadora=random.choice(frases_y_pelis) #tupla con frase y pelicula ganadora
        pelis_no_ganadoras= [p[1] for p in frases_y_pelis if p != op_ganadora] #Lista de todas las peliculas I= a op ganadora
        pelis_no_ganadoras1=sorted(set(pelis_no_ganadoras)) #eliminamos las opciones repetidas 
        opciones=random.sample(pelis_no_ganadoras1, k=2) #Lista de las dos opciones no ganadoras 
        opciones.append(op_ganadora[1]) #Le agregamos la opcion correcta a la Lista de opciones
        random.shuffle(opciones) #mezcla Las opciones
        print ("Adivine a que película pertenece la siguiente frase:",op_ganadora [0])
        print("Las opciones para elegir son: ")
        for i,j in zip(opciones, range(1,4)): #agrega numero a las opciones de peliculas
            print (j,i)
        opcion=int (input("Elija la opción correcta, ingresando 1, 2 o 3 : "))
        if opcion-1==opciones.index(op_ganadora[1]):
            print("¡¡Felicitaciones,la opción elegida es la correcta!!!")
        elif opcion-1!=opciones.index(op_ganadora[1]):
            if opcion!=1 and opcion!=2 and opcion!=3:
                print("El número ingresado no es una opción posible")
            else:
                print("La opción es incorrecta :( ")
    return("\n ¡ Gracias por participar!!!")

def guardar_opciones (opciones):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%d/%m/%y %H:%M")
    with open ("./data/registro_de_opciones_seleccionadas.txt","a") as archi:
        archi.write(f"Opciones: {opciones}, Fecha y hora {formatted_datetime}\n")

def mostrar_opciones_seleccionadas(archivo):
    try:
        with open (archivo, "r") as archi:
            linea=archi.read()
            print("Las opciones seleccionadas previamente son: ")
            print(linea+"\n")
    except FileNotFoundError:
        print("Aun no se ha registrado opciones. ")

def borrar_opciones (archivo):
    with open (archivo, "w") as archi:
        archi.write("")