import math

def trigonometric_functions(start, end, step):
    for x in range(start, end, step):
        yield math.sin(x), math.cos(x), math.tan(x)

def main():
    start = int(input("Podaj początek zakresu: "))
    end = int(input("Podaj koniec zakresu: "))
    step = int(input("Podaj krok: "))
    for sin, cos, tan in trigonometric_functions(start, end, step):
        print(f"sin({start}) = {sin}, cos({start}) = {cos}, tan({start}) = {tan}")
        start += step

if __name__ == "__main__":
    main()
