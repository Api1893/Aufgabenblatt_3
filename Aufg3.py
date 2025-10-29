#Aufgabe 3

import random
import time

def reaction_time():
    wartezeit = random.uniform(1, 5)   #Für zufällige Wartezeit
    print(f"Die Wartezeit beträgt: {wartezeit:.4f}")

    time.sleep(wartezeit)   #Funktion damit es diese Zeit abwartet

    start_time = time.time_ns()     #Ab hier startet die Zeit
    #print(f"Start Zeit " + str(start_time))

    eingabe = input("Go ")  #Wartet auf eingabe
    print(eingabe ," wurde gedrückt")

    #Sobald etwas eingegeben wurde, stoppt es die Zeit
    stop_time = time.time_ns()
    #print(f"Stop Zeit " + str(stop_time))

    #Umrechnung von Nanosekunden in Sekunden und Startzeit - Endzeit
    differenz = (stop_time - start_time)/1000000000
    print(f"Ausführungszeit in Sekunden: {differenz:.4f}")

reaction_time()