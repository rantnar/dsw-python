import os

def reverse_file(file):
    lines = file.readlines()
    with open("reversed.txt", "w") as reversed_file:
        for line in reversed(lines):
            reversed_file.write(line)

def main():
    try:
        file = open(input("Podaj nazwę pliku: "))
        reverse_file(file)
        file.close()
    except FileNotFoundError:
        print("Nie znaleziono pliku")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
