from flask import render_template, request, redirect, url_for
from modules.config import app
from modules.funciones import mostrar_lista_peliculas, trivia, guardar_opciones, mostrar_opciones_seleccionadas, borrar_opciones
import json

RUTA="./data/"
DIRECCION=RUTA + "frases_de_peliculas.txt"


try:
    mostrar_lista_peliculas(DIRECCION)            
except FileNotFoundError:
    with open(DIRECCION, "w") as archi:
        pass

@app.route("/", methods=['GET','POST'])
def trivia():
    if request.method == 'GET':
        frase = request.form['input_frase']
        lista_frases_pelis=trivia(DIRECCION)

        return redirect( url_for('home') )
    return render_template("home.html")



if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')