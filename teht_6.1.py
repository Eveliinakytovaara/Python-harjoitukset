# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan
# satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma,
# joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def nopanluku():
    x = random.randint(1, 6)
    return x

while True:
    silmaluku = nopanluku()
    print(silmaluku)
    if silmaluku == 6:
        break






