#Aufgabe 3
import random
import time

def reaction_time():
    wartezeit = random.uniform(1, 6)
    print(wartezeit)

    time.sleep(wartezeit)

    start_time = time.time_ns()
    print(f"Start Zeit " + str(start_time))

    eingabe = input("Go ")
    print(eingabe + " wurde gedrückt")

    stop_time = time.time_ns()
    print(f"Stop Zeit " + str(stop_time))

    differenz = stop_time - start_time
    print(f"Ausführungszeit in Millisekunden: {differenz:.4f}")

reaction_time()