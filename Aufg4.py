#Aufgabe 4
from random import choice, randint
from string import ascii_letters, digits

def passwort_generator():
    passwort = []       #Erzeugt eine leere Liste
    char_num = randint(8, 200)      #Legt mindest und maximal Zeichen fest

    #Zeichen und Zahlen werden zusammengesetzt
    strings_aus_zahlen_buchstaben = ascii_letters + digits

    for i in range(char_num+1):
        passwort.append(choice(strings_aus_zahlen_buchstaben))
    return "".join(passwort)        #.join ersetzt Zeichen

print(passwort_generator())