import numpy as np
import random
import matplotlib.pyplot as plt
import sympy as sp

class DetectorAlimento:
    """clase que representa un conjunto de sensores de la cinta transportadora
    para detectar el tipo de alimento y su peso.
    """
    def __init__(self):
        self.alimentos = ["kiwi", "manzana", "papa", "zanahoria", "undefined"]
        self.peso_alimentos = np.round(np.linspace(0.05, 0.6, 12),2)
        self.prob_pesos = np.round(self.__softmax(self.peso_alimentos)[::-1], 2)

    def __softmax(self, x):
        """función softmax para crear vector de probabilidades 
        que sumen 1 en total
        """
        return (np.exp(x - np.max(x)) / np.exp(x - np.max(x)).sum())

    def detectar_alimento(self):
        """método que simula la detección del alimento y devuelve un diccionario
        con la información del tipo y el peso del alimento.
        """
        n_alimentos = len(self.alimentos)
        alimento_detectado = self.alimentos[random.randint(0, n_alimentos-1)]
        peso_detectado = random.choices(self.peso_alimentos, self.prob_pesos)[0]
        return {"alimento": alimento_detectado, "peso": peso_detectado}
    
"""
if __name__ == "__main__":
    
    random.seed(1)
    sensor = DetectorAlimento()
    lista_pesos = []
    for _ in range(200):
        lista_pesos.append(sensor.detectar_alimento()["peso"])
    plt.hist(lista_pesos, bins=12)
    plt.show()
"""


class Alimento: #Todas sus instancias se agregar a cajón
    def __init__(self, dic):
        pass



class Fruta(Alimento):
    def __init__(self, dic):
        pass



class Manzana(Fruta): 
    def __init__(self, dic):
        self.nombre=dic['alimento']
        self.peso=dic['peso']
    def CalcularAW(self):
        c=15 #**(-1)
        return (0.97*(((c*self.peso)**2)/(1+(c*self.peso)**2)))




class Kiwi(Fruta):
    def __init__(self, dic):
        self.nombre=dic['alimento']
        self.peso=dic['peso']
    def CalcularAW(self):
        c=18#**(-1)
        return (0.96*((1-sp.exp(-(c*self.peso)))/(1+sp.exp(-(c*self.peso)))))




class Verdura(Alimento):
    def __init__(self, dic):
        pass



class Indefinido(Alimento):
    def __init__(self, dic):
       self.nombre=dic['alimento']
       self.peso=dic['peso']
    pass



class Papa(Verdura):
    def __init__(self, dic):
       self.nombre=dic['alimento']
       self.peso=dic['peso']
    def CalcularAW(self):
        c=18#**(-1)
        return (0.66*sp.atan(c*self.peso))
        



class Zanahoria(Verdura):
    def __init__(self, dic):
        self.nombre=dic['alimento']
        self.peso=dic['peso']
    def CalcularAW(self):
        c=10#**(-1) 
        return (0.96*(1-sp.exp(-(c*self.peso))))




class Cajón: #Se asocia con CintaTransportadora
    def __init__(self, n_elementos=int):
        self.elementos=[]
        self.n_elementos=n_elementos
        return
    def agregar(self, Alimento):
        Infed=[]
        if Alimento.nombre == 'undefined':
            print("No se pudo realizar el transporte")
            pass
#            self.Indef.append(Alimento)
#            rint("!!!!!"+self.Indef)
        elif self.n_elementos > len(self.elementos):
            self.elementos.append(Alimento)
        else:
            print("Cajón lleno")
#        print(self.elementos)
    def prom_aw(self, nombre_str_alimento=str):
        cont=0
        tot=0
        for e in self.elementos:
            if e.nombre == nombre_str_alimento:
                cont =+ 1
                tot =+ e.CalcularAW()
        if cont !=0 : 
            return tot/cont
        else: 
            return cont




class CintaTransportadora: #Contiene a la clase DetectorAlimento y utiliza la clase Alimentos
    def __init__(self):
        det=DetectorAlimento()
        self.detector=det
    def Transportar(self, cajón=Cajón):
        Detector=DetectorAlimento()
        if cajón.n_elementos > 0:
            a=self.detector.detectar_alimento()
            return a
        else:
            print("No se pudo realizar el transporte")
