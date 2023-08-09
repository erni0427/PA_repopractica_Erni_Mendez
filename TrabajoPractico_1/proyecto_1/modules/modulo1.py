# módulo para organizar funciones o clases utilizadas en nuestro proyecto
lista=[]
lista_sin_repe=[]

def mostrar_lista_peliculas(archivo_peliculas):
    """Función que lee el archivo con las frases de las peliculas y las muestra en una lista de tuplas
    """
    with open(archivo_peliculas, "r", encoding="utf-8") as archi: #el encoding se utiliza para caracteres especiales
        for linea in archi:
            frase, pelicula = linea.rstrip("\n").split(';')
            lista.append(pelicula)
            lista_sin_repe=set(lista) 
    return[(i+1,elemento) for i,elemento in enumerate (sorted(lista_sin_repe))] 

