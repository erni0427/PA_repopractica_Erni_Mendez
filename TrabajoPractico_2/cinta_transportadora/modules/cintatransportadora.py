from modules.detectoralimento import DetectorAlimento
from modules.cajon import  Cajon
class CintaTransportadora: #Contiene a la clase DetectorAlimento y utiliza la clase Alimentos
    def __init__(self):
        detector=DetectorAlimento()
        self.__detector=detector
    @property
    def detector(self):
        return(self.__detector)
    
    def Transportar(self, cajon=Cajon):
        Detector=DetectorAlimento()
        if cajon.n_elementos > 0: #verifica q no este vacio
            alimento_como_diccionario=self.__detector.detectar_alimento() #utiliza el detector almacenado en self.__detector para detectar un alimento y lo devuelve como un diccionario que contiene información sobre el tipo de alimento y su peso
            return alimento_como_diccionario
        else:
            print("No se pudo realizar el transporte")

