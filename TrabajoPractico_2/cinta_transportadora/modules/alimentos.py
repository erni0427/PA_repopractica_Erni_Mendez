import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from abc import ABC, abstractmethod

class Alimento(ABC): #Todas sus instancias se agregan a un cajón
    
    def __init__(self, peso):
        self.__peso= peso
    
    @abstractmethod
    def CalcularAW(self):
        pass
    
    @property
    def peso(self):
        return(self.__peso)


class Fruta(Alimento, ABC):
    def __init__(self):
        pass


class Manzana(Fruta): 
    def __init__(self, peso):
        super().__init__(peso)

    def CalcularAW(self):
        c=15 
        return (0.97*(((c*self.peso)**2)/(1+(c*self.peso)**2)))


class Kiwi(Fruta):
    def __init__(self, peso):
        super().__init__(peso)

    def CalcularAW(self):
        c=18#**(-1)
        return (0.96*((1-sp.exp(-(c*self.peso)))/(1+sp.exp(-(c*self.peso)))))


class Verdura(Alimento,ABC):
    def __init__(self):
        pass


class Papa(Verdura):
    def __init__(self, peso):
        super().__init__(peso)
    
    def CalcularAW(self):
        c=18#**(-1)
        return (0.66*sp.atan(c*self.peso))
        

class Zanahoria(Verdura):
    def __init__(self,peso):
        super().__init__(peso)

    def CalcularAW(self):
        c=10#**(-1) 
        return (0.96*(1-sp.exp(-(c*self.peso))))
    

class Indefinido(Alimento,ABC):
    def __init__(self, peso):
        super().__init__(peso)
