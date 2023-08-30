from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
from modules.funciones import  trivia
from modules.funcionesweb import fechaHora
import sys

RUTA="./data/"
DIRECCION=RUTA + "frases_de_peliculas.txt"
with open(DIRECCION,"r",encoding="utf-8") as archi: # utf-8 reconoce caracteres especiales en la Lista
        lista1=archi.readlines()
        lista_sin_repe=set(lista1)
        frases_y_pelis = [(linea.strip().split(';')[0], linea.strip().split(';')[1]) for linea in lista_sin_repe]

@app.route("/", methods=["GET", "POST"])
def raiz():
    """Esta función maneja la ruta de la página de inicio ("/"). Cuando se realiza una solicitud GET, muestra la plantilla "home.html". 
    Si se recibe una solicitud POST, toma los datos del formulario (el número de frases y el nombre de usuario) y redirige a la 
    función jugar() con los parámetros proporcionados. """

    global usuario, numero_frase
    if request.method == 'POST':
        numero_frase = int(request.form['input_num'])
        usuario = request.form['usuario']
        return redirect( url_for('jugar',usuario=usuario, numero_frase=numero_frase) )
    return render_template("home.html")

contador_r=0
contador_a=0
@app.route('/trivia', methods=["GET", "POST"])
def jugar():
    """Esta función maneja la ruta "/trivia". Recibe una solicitud GET o POST. Si es una solicitud GET, inicializa una sesión de juego
      y muestra una pregunta de trivia. Si es una solicitud POST, actualiza la sesión de juego con los datos proporcionados por el 
      formulario y muestra la siguiente pregunta de trivia. Cuando se ha completado el número especificado de rondas, redirige 
      de nuevo a la página de inicio. """
    global usuario, numero_frase,contador_a,contador_r
    lista=trivia(frases_y_pelis)
    if contador_r < int(numero_frase):
        contador_r +=1
        return render_template('trivia.html', usuario=usuario, frase=lista[0], correcta=lista[1],peliculas=lista[2] 
                               , numero_frase=numero_frase,contador_r=contador_r,contador_a=contador_a)     
    else: 
        return redirect(url_for('raiz'))

contador_r=0
contador_a=0

@app.route('/triviaans', methods=['POST'])
def triviaans():
    """Maneja la ruta "/triviaans". Recibe datos de respuesta del formulario, compara la respuesta proporcionada con la respuesta
      correcta y actualiza la puntuación y la ronda en la sesión. Luego, muestra una página que indica si la respuesta fue correcta
     o incorrecta. """
    global usuario, numero_frase,contador_r,contador_a
    correcta = request.form.get("correcta")
    respuesta = request.form.get("respuesta")
    if correcta==respuesta:
        contador_a+=1

    if contador_r==int(numero_frase):
        try:
            puntajes = open("data/puntajes.txt", "a")
            fechaFinal= fechaHora()
            renglon= usuario + "," + str(contador_a)+ "/"+str(numero_frase)+","+ str(fechaFinal)+ "\n"
            puntajes.write(renglon)
            puntajes.close()
        except:
            print("el archivo ''puntajes.txt'' no existe")
            sys.exit()
        
        #escribir archivo con datos de la sesion,formato usuario counter/round fecha inicio fecha final
    return render_template("triviaans.html",respuesta=respuesta,correcta=correcta,numero_frase=numero_frase,contador_r=contador_r,contador_a=contador_a)    

@app.route('/historicos', methods=['POST'])
def result():
    """Maneja la ruta "/historicos". Esta función se utiliza para mostrar los puntajes históricos de los jugadores. Lee el 
    archivo "puntajes.txt", parsea los datos de las sesiones anteriores y los almacena en una lista de diccionarios. Luego, 
    muestra esta información en la plantilla "historicos.html". """
    global usuario, numero_frase,contador_a,contador_r

    listaPuntajes=[]
    try:
        puntajes = open("data/puntajes.txt", "a")
        puntajes.close()
    except:
        puntajes = open("data/puntajes.txt", "a")
        puntajes.close()
        sys.exit() #función que se utiliza para terminar el programa de manera abrupta.

    with open("data/puntajes.txt", "r") as archi:
        for linea in archi:
            listaPuntaje = linea.rstrip().split(',')
            puntaje = {
                "usuario": listaPuntaje[0],
                "acertadas": listaPuntaje[1],
                "fechaFinal": listaPuntaje[2], 
            }
            listaPuntajes. append(puntaje)
    if len(listaPuntajes) == 0:
        return render_template("historicos.html", esta_vacia=True)
    return render_template("historicos.html", esta_vacia=False, listaPuntajes=listaPuntajes )


if __name__=="__main__":
    app.run(debug=True)