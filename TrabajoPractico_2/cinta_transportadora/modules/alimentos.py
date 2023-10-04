import sympy as sp
from abc import ABC, abstractmethod

class Alimento(ABC): #Todas sus instancias se agregan a un cajón
    
    def __init__(self, peso):
        if isinstance(peso, float) and peso>=0.05 and peso<=0.6:
            self.__peso= peso
        else:
            raise ValueError("El peso debe ser un número decimal (float) y estar en el rango posible")
    
    @property
    def peso(self):
        return(self.__peso)
    
    @abstractmethod
    def calcularAW(self): 
        pass

    @abstractmethod
    def __str__(self):
        pass


class Fruta(Alimento, ABC):
    def __init__(self,peso):
        super().__init__(peso)


class Manzana(Fruta): 
    def __init__(self, peso):
            super().__init__(peso)



    def calcularAW(self):
        c=15 
        return (0.97*(((c*self.peso)**2)/(1+(c*self.peso)**2)))
    
    def __str__(self):
        return "Manzana"



class Kiwi(Fruta):
    def __init__(self, peso):
            super().__init__(peso)

    def calcularAW(self):
        c=18#**(-1)
        return (0.96*((1-sp.exp(-(c*self.peso)))/(1+sp.exp(-(c*self.peso)))))
    
    def __str__(self):
        return "Kiwi"


class Verdura(Alimento,ABC):
    def __init__(self,peso):
        super().__init__(peso)


class Papa(Verdura):
    def __init__(self, peso):
            super().__init__(peso)
    
    def calcularAW(self):
        c=18#**(-1)
        return (0.66*sp.atan(c*self.peso))
    
    def __str__(self):
        return "Papa"
        

class Zanahoria(Verdura):
    def __init__(self,peso):
            super().__init__(peso)
        

    def calcularAW(self):
        c=10#**(-1) 
        return (0.96*(1-sp.exp(-(c*self.peso))))
    
    def __str__(self):
        return "Zanahoria"
    

# if __name__=="__main__":
#     manzana=Manzana(-0.5)
#     print(manzana.calcularAW())
    

