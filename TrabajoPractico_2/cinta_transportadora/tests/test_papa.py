import unittest as ut
from modules.alimentos import Papa

class TestPapa(ut.TestCase):
    def test_aw_papa_con_005(self):
        papa=Papa(0.05)
        a=papa.calcularAW()
        self.assertAlmostEqual(a, 0.4837,3)
    
    def test_aw_papa_con_negativo_y_str(self):
        self.assertRaises(ValueError,Papa, -0.1)
        self.assertRaises(ValueError,Papa, "hola")

if __name__=='__main__':
    ut.main()