# módulo para organizar funciones o clases utilizadas en nuestro proyecto
import random
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

# Generar una trivia
def generar_trivia(archivo_peliculas, num_preguntas):
    trivia = random.sample(archivo_peliculas, num_preguntas)
    return trivia

# Mostrar y validar opciones
def mostrar_y_validar_opciones(lista_sin_repe, opciones):
    print("\n" + lista_sin_repe)
    random.shuffle(opciones)
    for idx, opcion in enumerate(opciones):
        print(f"{idx + 1} - {opcion}")
    
    respuesta_correcta = opciones.index(lista_sin_repe)
    while True:
        try:
            seleccion = int(input("Selecciona la opción correcta (1/2/3): "))
            if seleccion < 1 or seleccion > 3:
                print("Por favor, selecciona una opción válida.")
            else:
                if seleccion == respuesta_correcta + 1:
                    print("¡Correcto! ¡Felicitaciones!\n")
                else:
                    print(f"Incorrecto. La respuesta correcta era: {respuesta_correcta + 1} - {lista_sin_repe}\n")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")