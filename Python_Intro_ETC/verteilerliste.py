#!usr/bin/env python3

"""Projektname: Verteilerliste 
    Anforderungen: 
    * Auflisten der Liste
    * Suchen in der Liste
    * Einfügen in der Liste
    * Löschen in der Liste
    
    Listeninhalte: 
    * Rufnummer (01 2345678)
    *Equipmentposition (bsp. Links/Rechts/Oben/Unten)
    * Type (Bsp. Pager, Phone, Mobile,...)
    
    Ansätze:
    *definieren einer fixen Datenstruktur
    * die Funktionen definieren (ev. mit pass)
    *Implementieren der Funktionen
    * Fertigprogrammieren

    Definitionen: 
    * geänderte Liste muss nicht gespeichert werden 
    * Wie kann ich den Benutzer fragen was er tun möchte. 
    * Wie in einem Textfile abspeichern / muss auch wieder lesbar sein!
    * think kabout JSON oder YAML (YAML is nur vollständigkeitshalber erwähnt) format (JSON is better supported!)
    + pickle wird nur von Python supported,  
"""

verteilerliste = [
    1254546,
    "links",
    "Pager"
]


def operation():
    def auflisten():
        print(verteilerliste)

    def suchen(subi):
        if subi in verteilerliste:
            print("is in Verteilerliste!")
        else:
            print("is not in Verteilerliste!")

    def einfügen(einf):
        verteilerliste.append(einf)
        print(verteilerliste)

    def löschen(delete):
        verteilerliste.remove(delete)
        print(verteilerliste)
    return auflisten, suchen, einfügen, löschen


my_auflisten, my_suchen, my_einfügen, my_löschen = operation()

if __name__ == "__main__":

    input_user = input("auflisten, suchen, einfügen oder löschen?....")

    if input_user == "auflisten":
        my_auflisten()
    elif input_user == "suchen":
        word = input("Was wird gesucht?")
        my_suchen(word)
    elif input_user == "einfügen":
        word = input("Welches Wort soll eingefügt werden?")
        my_einfügen(word)
    elif input_user == "löschen":
        word = input("Was soll gelöscht werden?")
        my_löschen(word)
    else:
        print("falsche Eingabe bitte nochmal starten")
