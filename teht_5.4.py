# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa
# järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen
# ja for/in toistorakennetta niiden läpikäymiseen.

City = []


for i in range(1, 6):
    userCity = input("Anna kaupungin nimi: ")
    City.append(userCity)

print("Tässä on lista kaupungeista: ")
for citylist in City:
    print(citylist)




