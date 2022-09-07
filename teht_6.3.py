# Kirjoita funktio, joka saa parametrinaan bensiinin määrän
# Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.

def gallonmaara(gallon):
    x = maara * 3.785
    return x

gallon = 3.785
maara = float(input("Anna määrä galloneina: "))
while maara > -1:
    litrat = gallonmaara(gallon)
    print(litrat)
    maara = float(input("Anna määrä galloneina: "))
else:
    print("negatiivinen luku")





