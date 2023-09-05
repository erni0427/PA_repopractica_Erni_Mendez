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

def trivia (lista_frases_pelis,frases_utilizadas=set()):
    """Función que extrae 3 películas y 1 frase al azar y retorna frase y pelicula ganadora ademas de las 3 opciones de peliculas"""
    # Filtramos las frases que aún no han sido utilizadas
    frases_disponibles = [p for p in lista_frases_pelis if p not in frases_utilizadas]
    
    # Si no hay más frases disponibles, reiniciamos el conjunto de frases utilizadas
    if not frases_disponibles:
        frases_utilizadas.clear()
        frases_disponibles = lista_frases_pelis
    
    # Seleccionamos una frase al azar de las disponibles
    op_ganadora = random.choice(frases_disponibles)
    
    # Agregamos la frase utilizada al conjunto
    frases_utilizadas.add(op_ganadora)
    
    # Filtramos las películas no ganadoras
    pelis_no_ganadoras = [p[1] for p in lista_frases_pelis if p[0] != op_ganadora[0]]
    
    # Eliminamos las opciones repetidas
    pelis_no_ganadoras_unicas = sorted(set(pelis_no_ganadoras))
    
    # Elegimos dos opciones no ganadoras al azar
    opciones = random.sample(pelis_no_ganadoras_unicas, k=2)
    
    # Agregamos la opción correcta a la lista de opciones
    opciones.append(op_ganadora[1])
    
    # Mezclamos las opciones
    random.shuffle(opciones)
    
    lista = [op_ganadora[0], op_ganadora[1], opciones]
    return lista

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