import unittest as ut
from modules.funcion import detectar
from modules.cajon import Cajon
from modules.cintatransportadora import CintaTransportadora
from modules.alimentos import Alimento

class TestCajon(ut.TestCase):
    def test_my_cajon(self):
        cajon1=Cajon(1)
        cinta1=CintaTransportadora()
        while 1 > len(cajon1.elementos):
           alimento_detectado=cinta1.Transportar(cajon1)
           alimento_definido=detectar(alimento_detectado)
           if isinstance(alimento_definido,Alimento):
                cajon1.agregar(alimento_definido)    
        #primer_alimento_lista=cajon1.elementos[0]
        #self.assertIsNotNone(primer_alimento_lista)
        self.assertIn(alimento_definido, cajon1.elementos)

if __name__=='__main__':
    ut.main()
