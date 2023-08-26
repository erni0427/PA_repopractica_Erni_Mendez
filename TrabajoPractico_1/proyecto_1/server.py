from flask import Flask, render_template, request, redirect, url_for
app = Flask("server")
from modules.funciones import mostrar_lista_peliculas, trivia, guardar_opciones, mostrar_opciones_seleccionadas, borrar_opciones
from modules.funcionesweb import fechaHora
import json
import sys

RUTA="./data/"
DIRECCION=RUTA + "frases_de_peliculas.txt"
with open(DIRECCION,"r",encoding="utf-8") as archi: # utf-8 reconoce caracteres especiales en la Lista
        lista1=archi.readlines()
        frases_y_pelis = [(linea.strip().split(';')[0], linea.strip().split(';')[1]) for linea in lista1]
counter=0

@app.route("/", methods=["GET", "POST"])
def raiz():
    global numero_frase
    global usuario
    if request.method == 'POST':
        numero_frase = request.form['input_num']
        usuario = request.form['usuario']
        return redirect( url_for('jugar',usuario=usuario, numero_frase=numero_frase) )
    return render_template("home.html")

@app.route('/trivia', methods=["GET", "POST"])
def jugar():
    sesion = {
        "round": int(request.form.get("round")) if request.form.get("round") is not None else 0,
        "acertadas": int(request.form.get("acertadas")) if request.form.get("acertadas") is not None else 0,
        # Otros datos de la sesión
    }
    lista=trivia(frases_y_pelis)
    sesion["round"] +=1
    if sesion["round"] <= int(numero_frase):
        return render_template('trivia.html', usuario=usuario, frase=lista[0], correcta=lista[1],peliculas=lista[2] ,sesion=sesion)     
    else:
        return render_template("home.html")     


@app.route('/triviaans', methods=['POST'])
def triviaans():
    sesion = {
        "round": int(request.form.get("round")) if request.form.get("round") is not None else 0,
        "acertadas": int(request.form.get("acertadas")) if request.form.get("acertadas") is not None else 0,
        # Otros datos de la sesión
    }
    correcta = request.form.get("correcta")
    respuesta = request.form.get("respuesta")
    if correcta==respuesta:
        sesion["acertadas"]+=1
    if sesion["round"]==numero_frase:
        try:
            puntajes = open("data/puntajes.txt", "a")
        except:
            print("el archivo ''puntajes.txt'' no existe")
            sys.exit()
        fechaFinal= fechaHora()
        sesion["fechaFinal"]=fechaFinal
        renglon= sesion["nombre"] + "," + str(sesion["acertadas"])+ "/"+numero_frase+","+sesion["fechaInicio"]+","+ sesion ["fechaFinal"]+ "\n"
        puntajes.write(renglon)
        puntajes.close()
        #escribir archivo con datos de la sesion,formato usuario counter/round fecha inicio fecha final
        
    return render_template("triviaans.html",respuesta=respuesta,correcta=correcta, sesion=sesion)

@app.route('/triviainit', methods=['POST'])
def triviainit():
    usuario = request.form.get("nombre")
    fechaInicio= fechaHora()
    #round = 1
    sesion = {
            "usuario": usuario,
            "fechaInicio": fechaInicio,
            "acertadas": "",
            "round": "", 
            "fechaFinal": "",
        }
    frase, peli, triviapeli = trivia(frases_y_pelis)
    return render_template('trivia.html', frase=frase, correcta=peli, peliculas=triviapeli, sesion=sesion)     
#**sesion pasa todas las variables del diccionario por separado hechas string
@app.route('/historicos', methods=["GET", "POST"])
def resultados_historicos():
    return render_template('historicos.html')

@app.route('/resultados', methods=["GET", "POST"])
def resultados():
    return render_template('resultados.html')


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')