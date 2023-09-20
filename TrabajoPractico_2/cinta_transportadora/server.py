from flask import Flask, render_template, request
from modules.funcion import detectar
#from modules.alimentos import Alimento, Papa, Manzana, Fruta, Verdura, Kiwi, Indefinido
from modules.cajon import Cajon
from modules.cintatransportadora import CintaTransportadora
#from modules.detector import DetectorAlimento
from modules.alimentos import Kiwi, Manzana, Fruta, Zanahoria, Papa, Verdura, Alimento
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method =="POST":     #el código extrae el número total de alimentos en el cajón desde el formulario web.
        numero_total_alimentos_cajon=request.form['n'] 
        numero_total_alimentos_cajon=int(numero_total_alimentos_cajon) 
        cinta1=CintaTransportadora() #crea instancias de CintaTransportadora y Cajon con el número total de alimentos especificado.
        cajon1=Cajon(numero_total_alimentos_cajon)

        while numero_total_alimentos_cajon > len(cajon1.elementos): #e ejecuta un bucle que simula el transporte de alimentos desde la cinta transportadora al cajón hasta que se alcance el número total especificado
           alimento_detectado=cinta1.Transportar(cajon1)          #se detectan
           alimento_definido=detectar(alimento_detectado)
           if isinstance(alimento_definido,Alimento): #verificar si un objeto es una instancia de una clase específica
                cajon1.agregar(alimento_definido)
        aw_k=cajon1.prom_aw(Kiwi)
        aw_m=cajon1.prom_aw(Manzana)
        aw_p=cajon1.prom_aw(Papa)
        aw_z=cajon1.prom_aw(Zanahoria)
        aw_F=cajon1.prom_aw(Fruta)
        aw_V=cajon1.prom_aw(Verdura)
        aw_T=cajon1.prom_aw(Alimento)

        aw_k=round(aw_k,4)
        aw_m=round(aw_m,4)
        aw_p=round(aw_p,4)  #redondear un número decimal al valor más cercano, 
        aw_z=round(aw_z,4)
        aw_F=round(aw_F,4)
        aw_V=round(aw_V,4)
        aw_T=round(aw_T,4)

        lista=[aw_F, aw_V, aw_m, aw_k, aw_p, aw_z, aw_T]
        
        return render_template("home.html", lista=lista, aw_F=aw_F , aw_V=aw_V, aw_m=aw_m, aw_k=aw_k, aw_p=aw_p, aw_z=aw_z, aw_T=aw_T)
    else:
        return render_template("home.html", aw_F= "", aw_V="", aw_m="", aw_k="", aw_p="", aw_z="", aw_T="" )

if __name__ == "__main__":
  app.run(debug=True)