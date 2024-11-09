with open("gcd_functions.py", "w") as dosya:
    dosya.write("""
def GCD_modulo(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def GCD_substraction(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
    """)
with open("gcd_tests.py", "w") as dosya:
    dosya.write("""
import unittest
from gcd_functions import GCD_modulo, GCD_substraction

class TestGCD(unittest.TestCase):
    def test_gcd_modulo(self):
        # GCD_modulo fonksiyonunu çeşitli testlerle kontrol et
        self.assertEqual(GCD_modulo(103, 3), 1)
        self.assertEqual(GCD_modulo(106, 3), 1)
        self.assertEqual(GCD_modulo(1010, 3), 1)
    
    def test_gcd_substraction(self):
        # GCD_substraction fonksiyonunu çeşitli testlerle kontrol et
        self.assertEqual(GCD_substraction(103, 3), 1)
        self.assertEqual(GCD_substraction(106, 3), 1)
        self.assertEqual(GCD_substraction(1010, 3), 1)

if __name__ == "__main__":
    unittest.main()
    """)
with open("performance_test.py", "w") as dosya:
    dosya.write("""
import timeit
from gcd_functions import GCD_modulo, GCD_substraction

# Test edilecek sayı çiftleri
numbers = [(103, 3), (106, 3), (1010, 3)]

# Her sayı çifti için GCD fonksiyonlarının sürelerini karşılaştır
for a, b in numbers:
    # GCD_modulo fonksiyonunun çalışma süresi
    time_modulo = timeit.timeit(lambda: GCD_modulo(a, b), number=1000)
    
    # GCD_substraction fonksiyonunun çalışma süresi
    time_substraction = timeit.timeit(lambda: GCD_substraction(a, b), number=1000)
    
    print(f"Numbers: ({a}, {b})")
    print(f"GCD_modulo execution time: {time_modulo:.5f} seconds")
    print(f"GCD_substraction execution time: {time_substraction:.5f} seconds\n")
    """)
    if __name__ == "__main__":
        import timeit
from gcd_functions import GCD_modulo, GCD_substraction

numbers = [(103, 3), (106, 3), (1010, 3)]

for a, b in numbers:
    time_modulo = timeit.timeit(lambda: GCD_modulo(a, b), number=1000)
    time_substraction = timeit.timeit(lambda: GCD_substraction(a, b), number=1000)
    print(f"Numbers: ({a}, {b})")
    print(f"GCD_modulo execution time: {time_modulo:.5f} seconds")
    print(f"GCD_substraction execution time: {time_substraction:.5f} seconds\n")
git add .

