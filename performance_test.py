
import timeit
from gcd_functions import GCD_modulo, GCD_substraction

# Test edilecek say� �iftleri
numbers = [(103, 3), (106, 3), (1010, 3)]

# Her say� �ifti i�in GCD fonksiyonlar�n�n s�relerini kar��la�t�r
for a, b in numbers:
    # GCD_modulo fonksiyonunun �al��ma s�resi
    time_modulo = timeit.timeit(lambda: GCD_modulo(a, b), number=1000)
    
    # GCD_substraction fonksiyonunun �al��ma s�resi
    time_substraction = timeit.timeit(lambda: GCD_substraction(a, b), number=1000)
    
    print(f"Numbers: ({a}, {b})")
    print(f"GCD_modulo execution time: {time_modulo:.5f} seconds")
    print(f"GCD_substraction execution time: {time_substraction:.5f} seconds
")
    