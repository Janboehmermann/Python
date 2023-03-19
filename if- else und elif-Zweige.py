age=int(input("Bitte gebe dein Alter ein : "))

if age < 18:
    print("Achtung, der Nutzer ist Jünger als 18!")
    print("Ich gehöre ebenfalls zur if-Anweisung")
elif age==18:
    print("Der Nutzer ist exakt 18")
else:
    print("Der Nutzer ist volljährig!")
print("Programmende")
