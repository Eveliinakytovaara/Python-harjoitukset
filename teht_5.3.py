# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

kokonaisluku = int(input("Anna kokonaisluku: "))
luku = [2,3,4,5,5,6,7,8,9]
numerot = 0

for numerot in range(11):
    if kokonaisluku in luku:
        luku.remove(kokonaisluku)

for numerot in range(len(luku)):
    if kokonaisluku % luku[numerot] == 0:
        print("kokonaisluku ei ole alkuluku")
        break
    elif numerot == len(luku)-1:
        if kokonaisluku % kokonaisluku == 0 and kokonaisluku % 1 == 0:
            print("Kokonaisluku on alkuluku")
