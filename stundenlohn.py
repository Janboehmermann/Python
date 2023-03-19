stundenlohn=input ("Bitte gebe deinen Stundenlohn ein: ")
tag=8 * int(stundenlohn)
monat=tag*20
jahr=monat*12

print ("Dein Stundenlohn beträgt " + str(stundenlohn) + "€")
print("Du verdienst " + str(tag) + "€ pro Tag.")
print ("Du verdienst " + str(monat) + "€ im Monat")
print("Du verdienst " +str(jahr) + "€ im Jahr")
input ("Taste drücken zum beenden!")