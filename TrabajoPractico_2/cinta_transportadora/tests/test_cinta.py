import unittest as ut
from modules.cintatransportadora import CintaTransportadora
from modules.cajon import Cajon
from modules.alimentos import Alimento


class TestCintaTransportadora(ut.TestCase):

    def test_transportar(self):
        cinta=CintaTransportadora()
        cajon=Cajon()
        cinta.transportar(cajon)
        self.assertEqual(len(cajon),1)

        cinta.transportar(cajon)
        self.assertEqual(len(cajon),2)

        
        cinta.transportar(cajon)
        self.assertEqual(len(cajon),3)

        
        cinta.transportar(cajon)
        self.assertEqual(len(cajon),4)
        
        for i in cajon:
            self.assertIsInstance(i, Alimento)





if __name__=='__main__':
    ut.main()