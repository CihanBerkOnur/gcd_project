
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
    