# módulo para organizar funciones o clases utilizadas en nuestro proyecto
import random
import datetime


def mostrar_lista_peliculas(archivo_peliculas):
    """Función que lee el archivo con las frases de las peliculas y retorna una lista de tuplas
    """
    lista=[]
    lista_sin_repe=[]
    with open(archivo_peliculas, "r", encoding="utf-8") as archi: #el encoding se utiliza para caracteres especiales
        for linea in archi:
            frase, pelicula = linea.rstrip("\n").split(';')
            lista.append(pelicula)
    lista_sin_repe=set(lista)
    return [(i+1, elemento) for i,elemento in enumerate (sorted(lista_sin_repe))] #elemento no es variable

def trivia (lista_frases_pelis):
    """Función que extrae 3 películas y 1 frase al azar y retorna frase y pelicula ganadora ademas de las 3 opciones de peliculas"""
    op_ganadora=random.choice(lista_frases_pelis) #tupla con frase y pelicula ganadora
    pelis_no_ganadoras= [p[1] for p in lista_frases_pelis if p != op_ganadora] #Lista de todas las peliculas I= a op ganadora
    pelis_no_ganadoras1=sorted(set(pelis_no_ganadoras)) #eliminamos las opciones repetidas 
    opciones=random.sample(pelis_no_ganadoras1, k=2) #Lista de las dos opciones no ganadoras 
    opciones.append(op_ganadora[1]) #Le agregamos la opcion correcta a la Lista de opciones
    random.shuffle(opciones) #mezcla Las opciones
    lista=[op_ganadora[0],op_ganadora[1],opciones]
    return(lista)

def guardar_opciones (opciones):
    """Funcion que guarda las opciones seleccionadas por el usuario con el formato %d/%m/%y %H:%M"""
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%d/%m/%y %H:%M")
    with open ("./data/registro_de_opciones_seleccionadas.txt","a") as archi:
        archi.write(f"Opciones: {opciones}, Fecha y hora {formatted_datetime}\n")

def mostrar_opciones_seleccionadas(archivo):
    """Muestra la secuencia de opciones seleccionadas previamente, sin contar las opciones que 
    elige cuando está jugando a la trivia de películas"""
    try:
        with open (archivo, "r") as archi:
            linea=archi.read()
    except FileNotFoundError:
        with open (archivo, "w") as archi:
            linea=archi.write("")
    return(linea)

def borrar_opciones (archivo):
    """Elimina el contenido del historial de opciones del registro """
    with open (archivo, "w") as archi:
        archi.write("")