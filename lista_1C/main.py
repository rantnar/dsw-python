from lista_1C_zad1 import liczby_zespolone
from lista_1C_zad2 import kryptografia
from lista_1C_zad3 import liczby_zespolone
from lista_1C_zad4 import grafy
from lista_1C_zad5 import wyszukiwanie_tekstowe as wt

a = complex(1, 2)  # 1 + 2i
b = complex(3, 4)  # 3 + 4i

print("Dodawanie: ", liczby_zespolone.dodaj(a, b))
print("Odejmowanie: ", liczby_zespolone.odejmij(a, b))
print("Mnożenie: ", liczby_zespolone.pomnoz(a, b))
print("Dzielenie: ", liczby_zespolone.podziel(a, b))


tekst = "Ala ma kota"
przesuniecie = 3
klucz = 0b10101010


print("Szyfr Cezara: ", kryptografia.szyfr_cezara(tekst, przesuniecie))
print("Deszyfr Cezara: ", kryptografia.deszyfr_cezara(kryptografia.szyfr_cezara(tekst, przesuniecie), przesuniecie))
print("Szyfr Vigenerea: ", kryptografia.szyfr_vigenerea(tekst, "klucz"))
print("Deszyfr Vigenerea: ", kryptografia.deszyfr_vigenerea(kryptografia.szyfr_vigenerea(tekst, "klucz"), "klucz"))
print("Szyfr XOR: ", kryptografia.szyfr_xor(tekst, klucz))
print("Deszyfr XOR: ", kryptografia.deszyfr_xor(kryptografia.szyfr_xor(tekst, klucz), klucz))

krawedzie = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
G = grafy.stworz_graf(krawedzie)

print("Ścieżki od 1 do 4: ", grafy.znajdz_sciezki(G, 1, 4))
print("Stopnie wierzchołków: ", grafy.oblicz_stopnie_wierzcholkow(G))

grafy.rysuj_graf(G)

text = "ABKBABABCABABABADBAKBCABCABABMBABABABC"
pattern = "BAKBC"

print("Indeks początkowy wzorca (KMP): ", wt.knuth_morris_pratt(text, pattern))
print("Indeks początkowy wzorca (BM): ", wt.boyer_moore(text, pattern))
print("Wyniki wyszukiwania regex: ", wt.regex_search(text, pattern))
