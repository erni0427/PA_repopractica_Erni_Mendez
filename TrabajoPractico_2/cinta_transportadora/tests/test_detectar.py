import unittest as ut
from modules.funcion import detectar
from modules.cintatransportadora import CintaTransportadora
from modules.cajon import Cajón
from modules.alimentos import Alimento



class Testdetectar(ut.TestCase):
    
    def test_my_detectar(self):
        cinta1=CintaTransportadora()
        cajon1=Cajón(1)
        alimento_detectado=cinta1.Transportar(cajon1)
        alimento_definido=detectar(alimento_detectado)
        if isinstance(alimento_definido,Alimento):
            cajon1.agregar(alimento_definido)    
        primer_alimento_lista=cajon1.elementos[0]
        self.assertIsNotNone(primer_alimento_lista)

if __name__=='__main__':
    ut.main()