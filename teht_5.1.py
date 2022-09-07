# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

arpakuutiot = int(input("Kerro arpakuutioiden määrä: "))
summa = 0

for arpakuutiot in range(arpakuutiot):
    tulos = random.randint(1, 6)
    summa = summa + tulos
    print(tulos)
print(f" Arpakuutioiden summa on: {summa} ")




