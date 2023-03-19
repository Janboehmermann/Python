
age=int(input("Bitte gebe dein Alter ein : "))
day_of_month=3

if age < 18:
    print("Achtung, der Nutzer ist Jünger als 18!")
    print("Ich gehöre ebenfalls zur if-Anweisung")
elif age==18 and day_of_month==3:
    print("Heute ist dein Glückstag, den du hast in der Lotterie gewonnen!")
else:
    print("Der Nutzer ist volljährig!")
print("Programmende")
