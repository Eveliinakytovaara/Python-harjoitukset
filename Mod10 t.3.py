# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton
# metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Elevator:
    def __init__(self, alin, ylin, nyt):
        self.alin = alin
        self.ylin = ylin
        self.nyt = nyt


    def move_to_floor(self,kerros):
        if self.nyt < kerros:
            Elevator.floor_up(e)
        if self.nyt > kerros:
            Elevator.floor_down(e)


    def floor_up(self):
        while self.nyt != kerros:
            self.nyt += 1
            if self.nyt == kerros:
                print(self.nyt)


    def floor_down(self):
        while self.nyt != kerros:
            self.nyt -= 1
            if self.nyt == kerros:
                print(self.nyt)


class House:
    def __init__(self, alin, ylin, e_lkm, now):
        self.alin = alin
        self.ylin = ylin
        self.e_lkm = e_lkm
        self.now = now
        self.elevators = []
        for i in range(1, 5):
            self.elevators.append(Elevator(1, 10, 1))


    def fire(self):
        for e in self.elevators:
            e.move_to_floor(self.alin)


    def ride(self, e_num, kohde):
        elevator = self.elevators[e_num -1]
        print(f"Ajetaan hissiä {e_num}\n")
        elevator.move_to_floor(kohde)
        if kohde == 112:
            self.palo()
        elevator.move_to_floor(kohde)

# pääohjelma

kerros = 1
h = House(1, 12, 4, 1)
e = Elevator(1, 12, 1)
while kerros < 13:
    hissi = int(input("Valitse hissi: 1-4 "))
    kerros = int(input("Mihin kerrokseen halutaan mennä?: "))
    print(f"Käytit hissiä {hissi} ja olet kerroksessa {kerros}.")
    if hissi == 1 and kerros == 12:
        print("PALOHÄLYTYS!")
        h.fire()
        break
    else:
        h.ride(hissi, kerros)

