import unittest as ut
from modules.alimentos import Manzana

class TestManzana(ut.TestCase):
    def test_aw_manzana_con_01(self):
        manzana=Manzana(0.1)
        a=manzana.CalcularAW()
        self.assertAlmostEqual(a, 0.67153846, 3)

if __name__=='__main__':
    ut.main()