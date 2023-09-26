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
        cajon1=Cajon(numero_total_alimentos_cajon)

        while numero_total_alimentos_cajon > len(cajon1.elementos): #Se ejecuta un bucle que simula el transporte de alimentos desde la cinta transportadora al cajón hasta que se alcance el número total especificado
           alimento_detectado=cinta1.transportar(cajon1)          #se detectan
           alimento_definido=cinta1.detectar(alimento_detectado)
           if isinstance(alimento_definido,Alimento): #verificar si un objeto es una instancia de una clase específica
                cajon1.agregar(alimento_definido)
        actividad_prom={}
        actividad_prom=cajon1.aw_alimentos()
        lista=[actividad_prom['frutas'], actividad_prom['kiwis'],actividad_prom['manzanas'],actividad_prom['verduras'],actividad_prom['papas'],actividad_prom['zanahorias'],actividad_prom['total']]
        
        return render_template("home.html",  actividad_prom=actividad_prom, lista=lista)
    else:
        return render_template("home.html", actividad_prom="", lista="")

if __name__ == "__main__":
  app.run(debug=True)