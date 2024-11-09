
import unittest
from gcd_functions import GCD_modulo, GCD_substraction

class TestGCD(unittest.TestCase):
    def test_gcd_modulo(self):
        # GCD_modulo fonksiyonunu çeþitli testlerle kontrol et
        self.assertEqual(GCD_modulo(103, 3), 1)
        self.assertEqual(GCD_modulo(106, 3), 1)
        self.assertEqual(GCD_modulo(1010, 3), 1)
    
    def test_gcd_substraction(self):
        # GCD_substraction fonksiyonunu çeþitli testlerle kontrol et
        self.assertEqual(GCD_substraction(103, 3), 1)
        self.assertEqual(GCD_substraction(106, 3), 1)
        self.assertEqual(GCD_substraction(1010, 3), 1)

if __name__ == "__main__":
    unittest.main()
    