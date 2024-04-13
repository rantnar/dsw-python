def szyfr_cezara(tekst, przesuniecie):
    wynik = ""
    for znak in tekst:
        if znak.isalpha():
            ascii_offset = 65 if znak.isupper() else 97
            wynik += chr((ord(znak) - ascii_offset + przesuniecie) % 26 + ascii_offset)
        else:
            wynik += znak
    return wynik

def deszyfr_cezara(tekst, przesuniecie):
    return szyfr_cezara(tekst, -przesuniecie)

def szyfr_vigenerea(tekst, klucz):
    wynik = ""
    for i, znak in enumerate(tekst):
        if znak.isalpha():
            ascii_offset = 65 if znak.isupper() else 97
            przesuniecie = ord(klucz[i % len(klucz)].upper()) - 65
            wynik += chr((ord(znak) - ascii_offset + przesuniecie) % 26 + ascii_offset)
        else:
            wynik += znak
    return wynik

def deszyfr_vigenerea(tekst, klucz):
    wynik = ""
    for i, znak in enumerate(tekst):
        if znak.isalpha():
            ascii_offset = 65 if znak.isupper() else 97
            przesuniecie = ord(klucz[i % len(klucz)].upper()) - 65
            wynik += chr((ord(znak) - ascii_offset - przesuniecie) % 26 + ascii_offset)
        else:
            wynik += znak
    return wynik

def szyfr_xor(tekst, klucz):
    return "".join(chr(ord(znak) ^ klucz) for znak in tekst)

def deszyfr_xor(tekst, klucz):
    return szyfr_xor(tekst, klucz)