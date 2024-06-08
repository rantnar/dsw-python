
def count_words(file):
    words = {}
    for line in file:
        word = line.strip()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

def main():
    try:
        file = open(input("Podaj nazwę pliku: "))
        print(count_words(file))
        file.close()
    except FileNotFoundError:
        print("Nie znaleziono pliku")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
