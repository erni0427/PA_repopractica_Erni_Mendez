import unittest as ut
from modules.alimentos import Zanahoria

class TestZanahoria(ut.TestCase):
    def test_aw_zanahoria_con_04(self):
        zanahoria=Zanahoria({'alimento':'zanahoria', 'peso': 0.4})
        #a=round(zanahoria.CalcularAW, 5)
        a=zanahoria.CalcularAW()
        self.assertAlmostEqual(a, 0.94242, 3)

if __name__=='__main__':
    ut.main() 
    