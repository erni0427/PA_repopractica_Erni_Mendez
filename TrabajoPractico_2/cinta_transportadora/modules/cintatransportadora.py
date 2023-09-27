from modules.detectoralimento import DetectorAlimento
from modules.cajon import  Cajon
from modules.alimentos import Kiwi,Papa,Zanahoria,Manzana
class CintaTransportadora: #Contiene a la clase DetectorAlimento y utiliza la clase Alimentos
    def __init__(self):
        detector=DetectorAlimento()
        self.__detector=detector
        
    @property
    def detector(self):
        return(self.__detector)
    
    def transportar(self, cajon=Cajon):
        if cajon.n_elementos != 0: #verifica q no este vacio
            alimento_como_diccionario=self.detector.detectar_alimento() 
            #utiliza el detector almacenado en self.detector para detectar un alimento y lo devuelve como un diccionario 
            # que contiene información sobre el tipo de alimento y su peso
            return alimento_como_diccionario
        else:
            raise Exception("No se pudo realizar el transporte")
    
    def detectar(self,diccionario={}): #para identificar de que alimento se trata
        if diccionario['alimento'] == 'Kiwi': 
            kiwi=Kiwi(diccionario['peso']) 
            #Si el valor de 'alimento' en el diccionario es 'kiwi', la función crea una instancia de la clase Kiwi pasando el diccionario 
            # como argumento, y luego devuelve esa instancia.
            return kiwi
        elif diccionario['alimento'] == 'Papa': #me fijo en clave alim del dicc si es tipo papa, si es asi, crea obj papa c peso
            papa=Papa(diccionario['peso']) 
            return papa
        elif diccionario['alimento'] == 'Manzana':
            manzana=Manzana(diccionario['peso']) 
            return manzana
        elif diccionario['alimento'] == 'Zanahoria':
            zanahoria=Zanahoria(diccionario['peso']) 
            return zanahoria
        else:
            return('Indefinido')
        
#if __name__ == "__main__":