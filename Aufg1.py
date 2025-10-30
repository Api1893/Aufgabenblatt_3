#Aufgabe 1
import random
from traceback import print_tb

def zahlenraten():
    zufallszahl = random.randint(0, 127)
    print(f"Die zufällige Zahl ist {zufallszahl}")
    for durchlauf in range(7, 0, -1):
        eingabe = int(input("Gebe eine Zahl ein!"))
        if eingabe > zufallszahl:
            print("Gesuchte Zahl ist kleiner als die Eingabe")
            print(f"Noch {durchlauf - 1} versuche")
            if durchlauf == 1:
                print("Keine Versuche mehr")
                print("Die gesuchte Zahl war:", zufallszahl)
            continue

        elif eingabe < zufallszahl:
            print("Gesuchte Zahl ist größer als die Eingabe")
            print(f"Noch {durchlauf - 1} versuche")
            if durchlauf == 1:
                print("Keine Versuche mehr")
                print("Die gesuchte Zahl war:", zufallszahl)
            continue

        else:
            print("Zahl gefunden")
            print(f"Gesuchte Zahl war {eingabe}")
            break

zahlenraten()