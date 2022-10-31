# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen
# numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo
# tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja
# kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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

    def ride(self, e_num, kohde):
        elevator = self.elevators[e_num -1]
        print(f"Ajetaan hissiä {e_num}\n")
        elevator.move_to_floor(kohde)
kerros = 1

h = House(1, 10, 4, 1)
e = Elevator(1, 10, 1)
hissi = int(input("Valitse hissi: "))
kerros = int(input("Mihin kerrokseen halutaan mennä?: "))
e.move_to_floor(kerros)
h.ride(kerros, hissi)