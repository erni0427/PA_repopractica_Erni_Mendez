import unittest as ut
from modules.alimentos import Manzana

class TestManzana(ut.TestCase):
    def test_aw_manzana_con_01(self):
        manzana=Manzana(0.1)
        a=manzana.calcularAW()
        self.assertAlmostEqual(a, 0.67153846, 3)

    def test_aw_manzana_con_negativo_y_str(self):
        self.assertRaises(ValueError,Manzana, -0.1)
        self.assertRaises(ValueError,Manzana, "hola")

if __name__=='__main__':
    ut.main()