import unittest as ut
from modules.alimentos import Papa

class TestPapa(ut.TestCase):
    def test_aw_papa_con_005(self):
        papa=Papa(0.05)
        a=papa.CalcularAW()
        self.assertAlmostEqual(a, 0.4837,3)

if __name__=='__main__':
    ut.main()