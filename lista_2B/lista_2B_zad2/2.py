#Napisz funkcję, która wczytuje liczbę od użytkownika i oblicza jej silnię.
#Obsłuż wyjątki dla ujemnych wartości oraz nieprawidłowych danych wejściowych.

def factorial(n):
    if n < 0:
        raise ValueError("Liczba musi być dodatnia")
    if not isinstance(n, int):
        raise TypeError("Liczba musi być całkowita")
    return 1 if n == 0 else n * factorial(n - 1)

def main():
    try:
        n = int(input("Podaj liczbę: "))
        print(f"{n}! = {factorial(n)}")
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()
