#!/usr/bin/env python3

""" 
Programmiere den Spieleklassiker Schere Stein Papier 
auch als Schnick Schnack Schnuck 

Schere schlägt Papier 
Stein schlägt Schere 
Papier schlägt Stein 

Das Programm soll bei Start abfragen welches Symbol verwendet werden soll. 
Der Computer wählt zufällig eines der drei Symbole 
Danach soll ausgegeben werden, wer gewonnen hat oder ob es ein Unentschieden ist. 

Tipp: random.randint(1, 3) liefert eine Zufallszahl zwischen 1 und 3 
"""

import random
data = {
    1: "Schere",
    2: "Stein",
    3: "Papier"
}

final = {
    "Mensch": 0,
    "Computer": 0,
    "Unentschieden": 0
}

print(""" 
Dieses Spiel ist unter folgenden Namen bekannt: 
Schere, Stein, Papier oder scissors stone paper 
Schnick, Schnack, Schnuck 
usw. 
Dabei schlägt Schere - Papier, Stein - Schere und Papier - Stein 
""")
print("Wähle:")
for key, val in data.items():
print(f"{key}) {val}")

while True:
    try:
        human = int(input(
            "\nWähle 1 (Schere), 2 (Stein) oder 3 (Papier). Alles andere steht für beenden: "))
    except ValueError:
        human = 0

    if human not in [1, 2, 3]:
        print(f"Unentschieden: {final['Unentschieden']}, Mensch gewonnen: {final['Mensch']}, Computer gewonnen: "
              f"{final['Computer']}")
    break

computer = random.randint(1, 3)
winner = False
if (
    (human == 1 and computer == 3) or
    (human == 2 and computer == 1) or
    (human == 3 and computer == 2)
):
    winner = "Mensch"
    final["Mensch"] += 1
elif (
    (computer == 1 and human == 3) or
    (computer == 2 and human == 1) or
    (computer == 3 and human == 2)
):
    winner = "Computer"
    final["Computer"] += 1
else:
    final['Unentschieden'] += 1

if not winner:
    print(
        f"Mensch: {data[human]: <7s} und Computer: {data[computer]: <7s} -> Das Spiel ist unentschieden")
else:
    print(
        f"Mensch: {data[human]: <7s} und Computer: {data[computer]: <7s} -> Ergebnis {winner: <8s} hat gewonnen")
