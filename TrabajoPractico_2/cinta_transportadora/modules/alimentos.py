import numpy as np
import random
import matplotlib.pyplot as plt
import sympy as sp
from abc import ABC, abstractmethod
class Alimento(ABC): #Todas sus instancias se agregar a cajón
    def __init__(self, nombre, peso, dic):
        self.nombre= nombre
        self.peso= peso
    @abstractmethod
    def CalcularAW(self):
        pass


class Fruta(Alimento,ABC):
    def __init__(self, dic):
        pass



class Manzana(Fruta): 
    def __init__(self, dic):
        self.nombre=dic['alimento']
        self.peso=dic['peso']
    def CalcularAW(self):
        c=15 #**(-1)
        return (0.97*(((c*self.peso)**2)/(1+(c*self.peso)**2)))




class Kiwi(Fruta):
    def __init__(self, dic):
        self.nombre=dic['alimento']
        self.peso=dic['peso']
    def CalcularAW(self):
        c=18#**(-1)
        return (0.96*((1-sp.exp(-(c*self.peso)))/(1+sp.exp(-(c*self.peso)))))




class Verdura(Alimento,ABC):
    def __init__(self, dic):
        pass


"""
class Indefinido(Alimento,ABC):
    def __init__(self, dic):
       self.nombre=dic['alimento']
       self.peso=dic['peso']
    def CalcularAW(self):
        pass
    pass
"""



class Papa(Verdura):
    def __init__(self, dic):
       self.nombre=dic['alimento']
       self.peso=dic['peso']
    def CalcularAW(self):
        c=18#**(-1)
        return (0.66*sp.atan(c*self.peso))
        



class Zanahoria(Verdura):
    def __init__(self, dic):
        self.nombre=dic['alimento']
        self.peso=dic['peso']
    def CalcularAW(self):
        c=10#**(-1) 
        return (0.96*(1-sp.exp(-(c*self.peso))))