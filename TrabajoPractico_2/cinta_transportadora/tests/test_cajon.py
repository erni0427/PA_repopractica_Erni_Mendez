import unittest as ut
from modules.cajon import Cajon
from modules.cintatransportadora import CintaTransportadora
from modules.alimentos import Alimento, Manzana, Kiwi, Papa, Zanahoria

class TestCajon(ut.TestCase):
    def setUp(self):
        # Crea una instancia de Cajon para usar en las pruebas
        self.cajon = Cajon(n_elementos=10)  # Puedes ajustar el número de elementos según tus necesidades

    def test_agregar_alimento(self):
        # Prueba agregar un alimento al cajón
        manzana = Manzana(0.4)
        self.cajon.agregar(manzana)
        self.assertIn(manzana, self.cajon.elementos)  # Verifica que la manzana esté en el cajón

        # Prueba agregar un alimento "Indefinido" (debería generar una excepción)
        with self.assertRaises(Exception):
            self.cajon.agregar("Indefinido")

    def test_prom_aw(self):
        # Prueba el cálculo del promedio de aw para un tipo específico de alimento
        manzana1 = Manzana(0.40)
        manzana2 = Manzana(0.45)
        kiwi = Kiwi(0.25)

        self.cajon.agregar(manzana1)
        self.cajon.agregar(manzana2)
        self.cajon.agregar(kiwi)

        promedio_manzanas = self.cajon.prom_aw(Manzana)
        self.assertAlmostEqual(promedio_manzanas, 0.95, places=2)  # Verifica el promedio con tolerancia de 2 decimales

    def test_aw_alimentos(self):
        # Prueba el cálculo de aw para diferentes tipos de alimentos
        manzana = Manzana(0.40)
        kiwi = Kiwi(0.25)
        papa = Papa(0.50)

        self.cajon.agregar(manzana)
        self.cajon.agregar(kiwi)
        self.cajon.agregar(papa)

        aw_result = self.cajon.aw_alimentos()
        self.assertAlmostEqual(aw_result["aw_manzanas"], 0.94, places=2)
        self.assertAlmostEqual(aw_result["aw_kiwis"], 0.94, places=2)
        self.assertAlmostEqual(aw_result["aw_papas"], 0.96, places=2)


if __name__=='__main__':
    ut.main()
