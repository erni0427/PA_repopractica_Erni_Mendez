from modules.detectoralimento import DetectorAlimento
from modules.cajon import  Cajón
class CintaTransportadora: #Contiene a la clase DetectorAlimento y utiliza la clase Alimentos
    def __init__(self):
        detector=DetectorAlimento()
        self.__detector=detector
    @property
    def detector(self):
        return(self.__detector)
    
    def Transportar(self, cajón=Cajón):
        Detector=DetectorAlimento()
        if cajón.n_elementos > 0:
            alimento_como_diccionario=self.__detector.detectar_alimento()
            return alimento_como_diccionario
        else:
            print("No se pudo realizar el transporte")

