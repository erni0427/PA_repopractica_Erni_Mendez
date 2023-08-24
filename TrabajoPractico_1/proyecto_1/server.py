from flask import render_template, request, redirect, url_for
from modules.config import app
from modules.funciones import mostrar_lista_peliculas, trivia, guardar_opciones, mostrar_opciones_seleccionadas, borrar_opciones


RUTA="./data/"
DIRECCION=RUTA + "frases_de_peliculas.txt"
with open(DIRECCION,"r",encoding="utf-8") as archi: # utf-8 reconoce caracteres especiales en la Lista
        lista1=archi.readlines()
        frases_y_pelis = [(linea.strip().split(';')[0], linea.strip().split(';')[1]) for linea in lista1]

@app.route("/", methods=["GET", "POST"])
def raiz():
    global numero_frase
    global nombre
    if request.method == 'POST':
        numero_frase = request.form['input_num']
        nombre = request.form['input_nombre']
        return redirect( url_for('jugar',nombre=nombre) )
    return render_template("home.html")

@app.route('/trivia', methods=["GET", "POST"])
def jugar():
    lista=trivia(frases_y_pelis)
    #if request.method == 'POST': 
    return render_template('trivia.html', nombre=nombre,frase=lista[0], correcta=lista[1],peliculas=lista[2])     

@app.route('/historicos', methods=["GET", "POST"])
def resultados_historicos():
    return render_template('historicos.html')

@app.route('/resultados', methods=["GET", "POST"])
def resultados():
    return render_template('resultados.html')

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')