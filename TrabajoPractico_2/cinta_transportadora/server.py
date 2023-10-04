from flask import Flask, render_template, request
from modules.cajon import Cajon
from modules.cintatransportadora import CintaTransportadora
from modules.alimentos import Alimento
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method =="POST":     #el código extrae el número total de alimentos en el cajón desde el formulario web.
        numero_total_alimentos_cajon=request.form['n'] 
        numero_total_alimentos_cajon=int(numero_total_alimentos_cajon) 
        cinta1=CintaTransportadora() #crea instancias de CintaTransportadora y Cajon con el número total de alimentos especificado.
        cajon1=Cajon()

        while numero_total_alimentos_cajon > len(cajon1): #Se ejecuta un bucle que simula el transporte de alimentos desde 
            #la cinta transportadora al cajón hasta que se alcance el número total especificado
           alimento_definido=cinta1.transportar(cajon1)          #se detectan
           if isinstance(alimento_definido,Alimento): #verificar si un objeto es una instancia de una clase específica
                cajon1.agregar(alimento_definido)
        actividad_prom={}
        actividad_prom=cajon1.aw_alimentos() #calcula pronm de cajon1
        lista=[actividad_prom['aw_frutas'], actividad_prom['aw_kiwis'],actividad_prom['aw_manzanas'],actividad_prom['aw_verduras'],actividad_prom['aw_papas'],actividad_prom['aw_zanahorias'],actividad_prom['aw_total']]
        
        return render_template("home.html",  actividad_prom=actividad_prom, lista=lista)
    else:
        return render_template("home.html", actividad_prom="", lista="")

if __name__ == "__main__":
  app.run(debug=True)