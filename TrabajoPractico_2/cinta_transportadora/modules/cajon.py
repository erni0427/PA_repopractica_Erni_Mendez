from modules.alimentos import Alimento, Fruta, Verdura, Kiwi, Manzana, Papa, Zanahoria
class Cajon: #Se asocia con CintaTransportadora
    def __init__(self):
        self.__elementos=[]
        self.__indice_actual = 0
    
    @property
    def elementos(self):
        return(self.__elementos)
    @property
    def indice_actual(self):
        return(self.__indice_actual)
    
    @indice_actual.setter
    def indice_actual(self,indice_act:int):
        self.__indice_actual = indice_act
    
    def agregar(self, alimento): 
        if not isinstance(alimento, Alimento):
            raise Exception("No es un alimento") #verificar si la cant de elementos es> a la cant permitida
        self.elementos.append(alimento)              # si cumple agrega


    def prom_aw(self, tipo):
        contador=0
        total=0
        for i in self.elementos:
            if isinstance (i, tipo):
                contador += 1
                total += i.calcularAW()
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
    
    def __iter__(self): #se llama cuando se utiliza la función iter(cajon) para obtener un iterador desde el objeto cajon.
        self.indice_actual = 0  # Reiniciar el índice al inicio
        return self 
    #Devuelve self como el propio objeto iterador. Esto significa que la propia instancia de Cajon actuará como el 
    #iterador, y el método __next__ será llamado en esta misma instancia.

    def __next__(self): 
        # se llama en cada iteración del ciclo for para obtener el siguiente elemento.
        if self.indice_actual < len(self.elementos): 
            # Esto asegura que no intentemos acceder a elementos que están más allá de la cantidad de elementos reales en el cajón.
            elemento = self.elementos[self.indice_actual] 
            #Obtiene el elemento actual del cajón utilizando el índice actual.
            self.indice_actual += 1
            # Incrementa el índice actual en 1 para que en la próxima iteración se obtenga el siguiente elemento.
            return elemento
        raise StopIteration 
        #Cuando hemos recorrido todos los elementos del cajón, lanzamos la excepción StopIteration. 
        # Esto le indica al ciclo for que detenga la iteración, ya que no hay más elementos que recorrer.
    def __len__(self):
        return len(self.elementos)

if __name__ == "__main__":

    cajon = Cajon()
    cajon.agregar(Manzana(0.1))
    cajon.agregar(Kiwi(0.45))
    cajon.agregar(Papa(0.05))
    cajon.agregar(Zanahoria(0.4))

    for alimento in cajon:
        print(alimento)
