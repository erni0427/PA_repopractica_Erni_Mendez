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
    

    def transportar(self, cajon: Cajon):
        alimento_como_diccionario=self.detector.detectar_alimento()
        while(alimento_como_diccionario['alimento']=="Indefinido"):
            alimento_como_diccionario=self.detector.detectar_alimento() 
        if alimento_como_diccionario['alimento'] == 'Kiwi': 
            alimento=Kiwi(alimento_como_diccionario['peso']) 
            #Si el valor de 'alimento' en el diccionario es 'kiwi', la función crea una instancia de la clase Kiwi pasando el diccionario 
            # como argumento, y luego devuelve esa instancia.
        elif alimento_como_diccionario['alimento'] == 'Papa': #me fijo en clave alim del dicc si es tipo papa, si es asi, crea obj papa c peso
            alimento=Papa(alimento_como_diccionario['peso']) 
        elif alimento_como_diccionario['alimento'] == 'Manzana':
            alimento=Manzana(alimento_como_diccionario['peso']) 
        elif alimento_como_diccionario['alimento'] == 'Zanahoria':
            alimento=Zanahoria(alimento_como_diccionario['peso']) 
        cajon.agregar(alimento)

                    
        
if __name__ == "__main__":
    cinta=CintaTransportadora()
    cajon=Cajon()
    cinta.transportar(cajon)
    cinta.transportar(cajon)
    cinta.transportar(cajon)
    cinta.transportar(cajon)
    cinta.transportar(cajon)
    for alimento in cajon:
        print(alimento)