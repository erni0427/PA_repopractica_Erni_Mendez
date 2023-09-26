from modules.alimentos import Alimento, Fruta, Verdura, Kiwi, Manzana, Papa, Zanahoria
class Cajon: #Se asocia con CintaTransportadora
    def __init__(self, n_elementos=int):
        self.__elementos=[]
        self.__n_elementos=n_elementos
        return
    
    @property
    def elementos(self):
        return(self.__elementos)
    @property
    def n_elementos(self):
        return(self.__n_elementos)

    def agregar(self, alimento): #PREGUNTAR
        if self.n_elementos > len(self.elementos): #verificar si la cant de elementos es> a la cant permitida
            self.elementos.append(alimento)              # si cumple agrega
        else:
            raise Exception("Cajón lleno")

    def prom_aw(self, tipo):
        contador=0
        total=0
        for i in self.elementos:
            if isinstance (i, tipo):
                contador += 1
                total += i.CalcularAW()
        if contador !=0: 
            return total/contador #devuelve 0 xq no se encontraron elementos de ese tipo
        else: 
            return contador
    
    def aw_alimentos(self):
        
        actividad={"aw_manzanas" : round(self.prom_aw(Manzana),2),
            "aw_kiwis" : round(self.prom_aw(Kiwi),2),
            "aw_papas" : round(self.prom_aw(Papa),2),
            "aw_zanahorias" : round(self.prom_aw(Zanahoria),2),
            "aw_frutas" : round(self.prom_aw(Fruta),2),
            "aw_verduras" : round(self.prom_aw(Verdura),2),
            "aw_total" :  round(self.prom_aw(Alimento),2) 
        }
        return actividad