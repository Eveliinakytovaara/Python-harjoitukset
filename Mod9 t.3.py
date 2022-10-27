# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka
# saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa
# sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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


    def kulje(self, tunnit):
        self.kuljettu_matka = self.nopeus * tunnit + self.kuljettu_matka



New_car = Car("ABC-123", 142)
car2 = Car("JLP-830", 160)
car2.accelerate(30)
car2.car_info()
car2.kulje(3)

car2.accelerate(70)
car2.car_info()
car2.accelerate(50)
car2.kulje(4)

car2.car_info()
car2.accelerate(-200)

New_car.car_info()
car2.car_info()

