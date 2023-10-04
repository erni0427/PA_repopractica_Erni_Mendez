import unittest as ut
from modules.alimentos import Kiwi

class TestKiwi(ut.TestCase):
    def test_aw_kiwi_045(self):
        kiwi=Kiwi(0.45)
        a=kiwi.calcularAW()
        self.assertAlmostEqual(a, 0.9594, 3)
    
    def test_aw_kiwi_con_negativo_y_str(self):
        self.assertRaises(ValueError,Kiwi, -0.1)
        self.assertRaises(ValueError,Kiwi, "hola")

if __name__=='__main__':
    ut.main()
    