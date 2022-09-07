# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden
# lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.


numbers = []
readingNumbers = True

while readingNumbers:
    strInput = input("Anna luku: ")
    if strInput == "":
        readingNumbers = False
    else:
        numbers.append(int(strInput))
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(numbers[0:5])
