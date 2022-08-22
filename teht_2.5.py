#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten
#mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.


#naulat grammoina = 32 * 13,3
#leiviskät grammoina = 20*32*13,3g

leiviska = int(input("anna leiviskän määrä "))
naula =  int(input("anna naulan määrä "))
luoti = int(input("anna luodin määrä "))

#laskutoimitukset
leiviska_gr = leiviska * 20 * 32 * 13,3
naula_gr = naula * 32 * 13,3
luoti_gr = luoti * 13,3


#tulostukset
print (f" {leiviska} leiviskää painaa {leiviska_gr} grammaa ")
print (f" {naula} naulaa painaa {naula_gr} grammaa ")
print (f" {luoti} luotia painaa {luoti_gr} grammaa ")