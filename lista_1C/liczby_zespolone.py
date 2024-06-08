def sprawdz_argumenty(a, b):
    if not isinstance(a, complex) or not isinstance(b, complex):
        raise TypeError("Oba argumenty muszą być liczbami zespolonymi")

def dodaj(a, b):
    sprawdz_argumenty(a, b)
    return a + b

def odejmij(a, b):
    sprawdz_argumenty(a, b)
    return a - b

def pomnoz(a, b):
    sprawdz_argumenty(a, b)
    return a * b

def podziel(a, b):
    sprawdz_argumenty(a, b)
    if b == 0:
        raise ValueError("Nie można dzielić przez zero")
    return a / b