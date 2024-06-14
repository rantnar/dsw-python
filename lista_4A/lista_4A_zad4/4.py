#Napisz program, który wczytuje listę słów z pliku tekstowego i wypisuje 5
#najczęściej występujących słów oraz ich liczbę wystąpień. Użyj modułu
#collections

import os
import collections

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
        words = count_words(file)
        for word, count in collections.Counter(words).most_common(5):
            print(f"{word}: {count}")
        file.close()
    except FileNotFoundError:
        print("Nie znaleziono pliku")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
