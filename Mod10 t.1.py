# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän
# kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja
# kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille
# h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
# tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin
# ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

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


e = Elevator(1, 10 ,1)
kerros = int(input("Mihin kerrokseen halutaan mennä? "))
e.move_to_floor(kerros)