import unittest as ut
from modules.cintatransportadora import CintaTransportadora
from modules.cajon import Cajon
from modules.detectoralimento import DetectorAlimento
from modules.alimentos import Kiwi, Papa, Manzana, Zanahoria


class TestCintaTransportadora(ut.TestCase):

    def setUp(self):
        # Crea una instancia de CintaTransportadora para usar en las pruebas
        self.cinta = CintaTransportadora()

    def test_transportar(self):
        # Prueba que el método transportar devuelva un diccionario con "alimento" y "peso"
        resultado = self.cinta.transportar()
        self.assertIsInstance(resultado, dict)
        self.assertIn("alimento", resultado)
        self.assertIn("peso", resultado)

    def test_detectar(self):
        # Prueba la función de detección de alimentos
        kiwi_dict = {"alimento": "Kiwi", "peso": 0.1}
        papa_dict = {"alimento": "Papa", "peso": 0.2}
        manzana_dict = {"alimento": "Manzana", "peso": 0.3}
        zanahoria_dict = {"alimento": "Zanahoria", "peso": 0.4}
        indefinido_dict = {"alimento": "Indefinido", "peso": 0.5}

        self.assertIsInstance(self.cinta.detectar(kiwi_dict), Kiwi)
        self.assertIsInstance(self.cinta.detectar(papa_dict), Papa)
        self.assertIsInstance(self.cinta.detectar(manzana_dict), Manzana)
        self.assertIsInstance(self.cinta.detectar(zanahoria_dict), Zanahoria)
        self.assertEqual(self.cinta.detectar(indefinido_dict), 'Indefinido')




if __name__=='__main__':
    ut.main()