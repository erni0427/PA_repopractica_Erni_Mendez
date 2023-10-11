from abc import ABC, abstractmethod
from modules.gestorDB import GestorDB
from modules.reclamo import Reclamo

class Departamento(ABC):
    def _init_(self):
        self.__reclamos_depto = []
    
    @property
    def reclamos_depto(self):
        return self.__reclamos_depto
    
    @abstractmethod
    def levantar_reclamos_depto(gestordb:GestorDB):
        pass

    @abstractmethod
    def analitica(self):
        """Conoce todos los reclamos (los recibe), debe mostrar estadisticas sobre el numero de reclamos"""
        pass
  

class DptoEspecifico(Departamento):
    def _init_(self, reclamos_depto, nombre):
        super().__init__(reclamos_depto)
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
        
    def analitica(self):
        """Conoce todos los reclamos (los recibe), debe mostrar estadisticas sobre el numero de reclamos"""
        pass



class DptoTecnico(Departamento):
    """modela los datos de un departamento """
    def _init_(self,reclamos_depto):
       super().__init__(reclamos_depto)

    def analitica(self):
        """Conoce todos los reclamos (los recibe), debe mostrar estadisticas sobre el numero de reclamos"""
        pass
    
    def levantar_reclamos_depto(gestordb:GestorDB): #quitar reclamo
        
        pass

    def derivar_reclamo(self, reclamo:Reclamo):
        """Recibe un reclamo y devuelve un entero (segun el departamento)"""
        pass
