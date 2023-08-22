# módulo para organizar funciones o clases utilizadas en nuestro proyecto
import random

#lista=[]
#lista_sin_repe=[]


def mostrar_lista_peliculas(archivo_peliculas):
    """Función que lee el archivo con las frases de las peliculas y las muestra en una lista de tuplas
    """
    lista=[]
    with open(archivo_peliculas, "r", encoding="utf-8") as archi: #el encoding se utiliza para caracteres especiales
        for linea in archi:
            frase, pelicula = linea.rstrip("\n").split(';')
            lista.append( (frase,pelicula) )
        
        pelis=list(set([peli for frase, peli in lista]))
    #return [(i+1, pelicula) for i,pelicula in enumerate(sorted(pelis))] 
    return lista, pelis

# Generar una trivia
def generar_trivia(lista_peliculas, num_peliculas):
    """Recibe listado de peliculas y retorna num peliculas sin repetir"""
    trivia = random.sample(lista_peliculas, num_peliculas)
    return trivia

# Mostrar y validar opciones
def mostrar_y_validar_opciones(lista_peliculas, opciones_peliculas):
    print(lista_peliculas)
    random.shuffle(opciones_peliculas)
    for idx, opcion in enumerate(opciones_peliculas):
        print(f"{idx + 1} - {opcion}")
    
    respuesta_correcta = opciones_peliculas.index(lista_peliculas)
    