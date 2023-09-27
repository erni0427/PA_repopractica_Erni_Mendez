import numpy as np
import random
import matplotlib.pyplot as plt
import sympy as sp

class DetectorAlimento:
    """clase que representa un conjunto de sensores de la cinta transportadora
    para detectar el tipo de alimento y su peso.
    """
    def __init__(self):
        self.__alimentos = ["Kiwi", "Manzana", "Papa", "Zanahoria", "Indefinido"] 
        self.__peso_alimentos = np.round(np.linspace(0.05, 0.6, 12),2) #valores de peso
        self.__prob_pesos = np.round(self.__softmax(self.__peso_alimentos)[::-1], 2) #almacen prob asociadas a los pesos de los alimentos, se calculan con la función __softmax, que normaliza los pesos de manera que sumen 1 en total.
    
    @property
    def alimentos(self):
        return(self.__alimentos)
    
    @property
    def peso_alimentos(self):
        return(self.__peso_alimentos)
    
    @property
    def prob_pesos(self):
        return(self.__prob_pesos)


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


