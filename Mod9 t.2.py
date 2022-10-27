# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
# sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

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

    def accelerate(self, nopeuden_muutos):
        if 0 < self.nopeus + nopeuden_muutos < self.huippunopeus:
            self.nopeus = self.nopeus + nopeuden_muutos
        elif self.nopeus + nopeuden_muutos <= 0:
            self.nopeus = 0

New_car = Car("ABC-123", 142)
car2 = Car("JLP-830", 160)
car2.accelerate(30)
car2.car_info()


car2.accelerate(70)
car2.car_info()
car2.accelerate(50)


car2.car_info()
car2.accelerate(-200)

New_car.car_info()
car2.car_info()