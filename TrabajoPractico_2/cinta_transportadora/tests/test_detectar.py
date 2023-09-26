import unittest as ut
from modules.cintatransportadora import CintaTransportadora
from modules.cajon import Cajon
from modules.alimentos import Alimento
from modules.detectoralimento import DetectorAlimento



class Testdetectar(ut.TestCase):
    def setUp(self):
        # Crea una instancia de DetectorAlimento para usar en las pruebas
        self.detector = DetectorAlimento()

    def test_detectar_alimento(self):
        # Prueba que el método detectar_alimento devuelva un diccionario
        resultado = self.detector.detectar_alimento()
        self.assertIsInstance(resultado, dict)

        # Prueba que el diccionario tenga una clave "alimento" y una clave "peso"
        self.assertIn("alimento", resultado)
        self.assertIn("peso", resultado)

        # Prueba que el "alimento" en el diccionario esté en la lista de alimentos conocidos
        self.assertIn(resultado["alimento"], self.detector.alimentos)

        # Prueba que el "peso" en el diccionario esté dentro de los valores de peso conocidos
        self.assertTrue(0.05 <= resultado["peso"] <= 0.6)


if __name__=='__main__':
    ut.main()