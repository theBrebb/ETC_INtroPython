
"""
    Programmiere den Spieleklassiker Schere Stein Papier
    
    Schere 1 schlägt Papier 2
    Stein 3 schlägt Schere 1
    Papier 2 schlägt Stein 3
    Brunnen 4 schlägt Schere 1 und Stein 2
    
    Das Programm soll bei Start abfragen welches Symbol verwendet werden soll. 
    Der Computer wählt zufällig eines der drei Symbole
    Danach soll ausgegeben werden, wer gewonnen hat oder ob es ein Unentschieden ist. 
    
    Tipp: random.randint(1,4) liefert eine Zufallszahle zwischen 1 und 4    
"""

import random

# def: schere = 1, Papier = 2, Stein = 3, Brunnen = 4
dict1 = {
    "Schere": 1,
    "Papier": 2,
    "Stein": 3,
    "Brunnen": 4
}

# dict2 = {y: x for x, y in dict1.items()}

dict2 = {
    1: "Schere",
    2: "Papier",
    3: "Stein",
    4: "Brunnen"
}

while True:
    try:
        P1_input = input("Schere, Stein oder Papier?")
        P1 = dict1[P1_input]
    except KeyboardInterrupt:
        P1 = 5
        break

    if P1 not in [1, 2, 3, 4]:
        if P1 == 5:
            print("ES GIBT KEINEN BRUNNEN!! 🤬🤬🤬 nimm:")
            continue
        else:
            print("false", P1)
            break

    P2 = random.randint(1, 4)

    if (
        (P1 == 2) & (P2 == 3) or
        (P1 == 3) & (P2 == 2) or
        (P1 == 3) & (P2 == 1) or
        (P1 == 1) & (P2 == 4) or
        (P1 == 3) & (P2 == 4) or
        (P1 == 4) & (P2 == 2)

    ):
        print("Computer hat gewonnen!", "Player 1: ",
              dict2[P1], ", Computer: ", dict2[P2])
    elif (
        (P1 == 1) & (P2 == 2) or
        (P1 == 2) & (P2 == 3) or
        (P1 == 3) & (P2 == 1) or
        (P1 == 4) & (P2 == 1) or
        (P1 == 4) & (P2 == 3) or
        (P1 == 2) & (P2 == 4)
    ):
        print("Player 1 hat gewonnen!", "Player 1: ",
              dict2[P1], ", Computer: ", dict2[P2])
    else:
        print("Unentschieden!", "Player 1: ",
              dict2[P1], ", Computer: ", dict2[P2])
