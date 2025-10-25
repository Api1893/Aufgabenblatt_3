#Aufgabe 4
import random
import string


def passwort_generator():
    strings_aus_Buchstaben = string.ascii_letters
    print(strings_aus_Buchstaben)

    strings_aus_Zahlen = string.digits
    print(strings_aus_Zahlen)
    print("")

    for durchlauf in range(8):
        passwort = []
        passwort.append(random.choice(strings_aus_Buchstaben))
        passwort.append(random.choice(strings_aus_Zahlen))
        print(passwort, end="")

passwort_generator()
print("")