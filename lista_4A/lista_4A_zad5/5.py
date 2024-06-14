import string

def caesar_cipher(text, shift):
    alphabet = string.ascii_lowercase
    encrypted = ""
    for char in text:
        if char.isalpha():
            index = (alphabet.index(char.lower()) + shift) % 26
            encrypted += alphabet[index]
        else:
            encrypted += char
    return encrypted

def main():
    text = input("Podaj tekst: ")
    shift = int(input("Podaj przesunięcie: "))
    print(caesar_cipher(text, shift))

if __name__ == "__main__":
    main()
