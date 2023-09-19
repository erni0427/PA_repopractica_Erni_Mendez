import unittest as ut
from modules.alimentos import Kiwi

class TestKiwi(ut.TestCase):
    def test_aw_kiwi_045(self):
        kiwi=Kiwi({'alimento':'kiwi', 'peso': 0.45})
        a=kiwi.CalcularAW()
        self.assertAlmostEqual(a, 0.9594, 3)

if __name__=='__main__':
    ut.main()
    