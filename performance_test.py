
import timeit
from gcd_functions import GCD_modulo, GCD_substraction

# Test edilecek sayý çiftleri
numbers = [(103, 3), (106, 3), (1010, 3)]

# Her sayý çifti için GCD fonksiyonlarýnýn sürelerini karþýlaþtýr
for a, b in numbers:
    # GCD_modulo fonksiyonunun çalýþma süresi
    time_modulo = timeit.timeit(lambda: GCD_modulo(a, b), number=1000)
    
    # GCD_substraction fonksiyonunun çalýþma süresi
    time_substraction = timeit.timeit(lambda: GCD_substraction(a, b), number=1000)
    
    print(f"Numbers: ({a}, {b})")
    print(f"GCD_modulo execution time: {time_modulo:.5f} seconds")
    print(f"GCD_substraction execution time: {time_substraction:.5f} seconds
")
    