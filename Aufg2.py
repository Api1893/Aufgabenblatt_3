#Aufgabe 2
import time

def countdown(zahl):
    if zahl >= 1:
        for durchlauf in range(zahl, 0, -1):
            print(durchlauf)
            time.sleep(1)
        print("---Lift off---")
    else:
        print("Ungültige Eingabe, da Zahl ist kleiner als 1 ist")

eingabe = int(input("Gebe ein Zahl ein die >= 1 ist: "))
countdown(eingabe)