from flask import render_template, request, redirect, url_for
from modules.config import app
from modules.funciones import mostrar_lista_peliculas, trivia, guardar_opciones, mostrar_opciones_seleccionadas, borrar_opciones

RUTA="./data/"
DIRECCION=RUTA + "frases_de_peliculas.txt"


""""try:
    cargar_lista_desde_archivo(ARCHIVO, lista_libros)            
except FileNotFoundError:
    with open(ARCHIVO, "w") as archi:
        pass


@app.route("/")
def home():
    esta_vacia = False
    # opción 1
    # if request.method == 'POST':
    #     nombre = request.form['input_nombre']
    #     autor = request.form['input_autor']
    #     puntaje = request.form['input_puntaje']
    #     agregar_libro_a_lista(lista_libros, nombre, autor, puntaje)
    #     guardar_libro_en_archivo(ARCHIVO, nombre, autor, puntaje)

    if len(lista_libros) == 0:
        esta_vacia = True

    return render_template('home.html', esta_vacia=esta_vacia, lista_libros=lista_libros)

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    # opción 2
    if request.method == 'POST':
        nombre = request.form['input_nombre']
        autor = request.form['input_autor']
        puntaje = request.form['input_puntaje']
        agregar_libro_a_lista(lista_libros, nombre, autor, puntaje)
        guardar_libro_en_archivo(ARCHIVO, nombre, autor, puntaje)

        return redirect( url_for('home') )

    return render_template('agregar.html')


if _name=="main_":
    app.run(debug=True, host='0.0.0.0')"""