def words(file):
    for line in file:
        for word in line.split():
            yield ''.join(filter(str.isalnum, word))

def main():
    try:
        file = open(input("Podaj nazwę pliku: "))
        for word in words(file):
            print(word)
        file.close()
    except FileNotFoundError:
        print("Nie znaleziono pliku")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
