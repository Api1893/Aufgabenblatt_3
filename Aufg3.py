#Aufgabe 3

import random
import time

def reaction_time():
    # Für zufällige Wartezeit
    wartezeit = random.uniform(1, 5)
    print(f"Die Wartezeit beträgt: {wartezeit:.4f}")

    # Funktion damit es diese Zeit abwartet
    time.sleep(wartezeit)

    # Ab hier startet die Zeit
    start_time = time.time_ns()

    # Wartet auf eingabe
    eingabe = input("Go ")
    print(eingabe ," wurde gedrückt")

    #Sobald etwas eingegeben wurde, stoppt es die Zeit
    stop_time = time.time_ns()

    #Umrechnung von Nanosekunden in Sekunden und Startzeit - Endzeit
    differenz = (stop_time - start_time)/1000000000
    print(f"Ausführungszeit in Sekunden: {differenz:.4f}")

reaction_time()