#Aufgabe 4
from random import choice, randint
from string import ascii_letters, digits

def passwort_generator():
    passwort = []
    char_num = randint(8, 200)

    strings_aus_zahlen_buchstaben = ascii_letters + digits

    for i in range(char_num+1):
        passwort.append(choice(strings_aus_zahlen_buchstaben))
    return "".join(passwort)

print(passwort_generator())