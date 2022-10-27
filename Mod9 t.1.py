# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus,
# huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi
# ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton
# (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Car:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def car_info(self):
        print(f"Auton {self.rekisteritunnus} \n"
        f"Huippunopeus on {self.huippunopeus} km/h \n"
        f"Nopeus on {self.nopeus}km/h \n"
        f"Kuljettu matka on {self.kuljettu_matka}\n")


New_car = Car("ABC-123", 142)
car2 = Car("JLP-830", 160)

New_car.car_info()
car2.car_info()