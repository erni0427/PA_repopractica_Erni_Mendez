import unittest as ut
from modules.alimentos import Zanahoria

class TestZanahoria(ut.TestCase):
    def test_aw_zanahoria_con_04(self):
        zanahoria=Zanahoria(0.4)
        a=zanahoria.calcularAW()
        self.assertAlmostEqual(a, 0.94242, 3)
    
    def test_aw_zanahoria_con_negativo_y_str(self):
        self.assertRaises(ValueError,Zanahoria, -0.1)
        self.assertRaises(ValueError,Zanahoria, "hola")

if __name__=='__main__':
    ut.main() 
    