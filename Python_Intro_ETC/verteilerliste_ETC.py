#!/usr/bin/env python3
import json
"""Projektname: Verteilerliste 
Anforderungen: 
* Auflisten der Liste 
* Suchen in der Liste 
* Einfügen in der Liste 
* Ändern in der Liste 
* Löschen in der Liste 

Listeninhalt: 
* Rufnummer (Bsp: 01345432, ...) 
* Equipmentposition (Bsp: Links, Rechts, Oben, Unten, ...) 
* Type (Bsp: Pager, Phone, Mobile, ...) 

Ansätze: 
Definieren einer fixen Datenstruktur 
Die Funktionen definieren (ev. mit pass) 
Implementieren der Funktionen 
Fertigprogrammieren 

Definitionen: 
Geänderte Liste muss nicht gespeichert werden 

+ beim Starten fragen 
+ wenn User speichern will soll man speichern 
"""


def print_datalist(data: list) -> None:
    """Print the datalist formatted"""
    col_width = [20, 20, 20]
    print_str = f"{'Callnumber': <{col_width[0]}}"
    print_str += f"{'Equipment position': <{col_width[1]}}"
    print_str += f"{'Type': <{col_width[2]}}"
    print_str += "\n"
    for item in data:
        print_str += f"{item['callnumber']: <{col_width[0]}}"
        print_str += f"{item['equipment_position']: <{col_width[1]}}"
        print_str += f"{item['type']: <{col_width[2]}}"
        print_str += "\n"

        print(print_str)


def print_founded(data) -> None:
    """Search for strings in datalist and print founded out"""
    foundlist = []
    search = input("Suchen: ")
    for item in data:
        for field in item.items():
            if search in field[1] and item not in foundlist:
                foundlist.append(item)

    print_datalist(foundlist)


def get_position_by_callnumber(data: list, callnumber: str) -> int:
    """return the position number in the datalist of callnumber"""
    counter = 0
    for item in data:
        if item["callnumber"] == callnumber:
            return counter
        counter += 1
    return -1


def print_menu() -> None:
    """print the menu for the user"""
    print("Auswahl:")
    print("1) Löschen")
    print("2) Ändern")
    print("3) Neu")
    print("4) Suchen")
    print("5) Auflisten")
    print("6) Speichern")
    print("7) Ende")


def find_item_number(data: list) -> int:
    """return the item position number to delete"""
    while True:
        callnumber = input("Bitte geben Sie die Rufnummer ein: ")
        pos_num = get_position_by_callnumber(data, callnumber)
        if pos_num == -1:
            continue
        else:
            break
    return pos_num


def get_new_item() -> dict:
    """ask for data for a new item"""
    callnumber = input("Bitte Rufnummer eingeben: ")
    equipment_position = input("Bitte Equipment position eingeben: ")
    item_type = input("Bitte Typ eingeben: ")
    return {
        "callnumber": callnumber,
        "equipment_position": equipment_position,
        "type": item_type
    }


def get_changed_item(data: dict) -> dict:
    """ask for data for a new item"""
    callnumber_prompt = f"Bitte Rufnummer eingeben [{data['callnumber']}]: "
    callnumber = input(callnumber_prompt) or data['callnumber']
    equipment_position_prompt = f"Bitte Equipment position eingeben [{data['equipment_position']}]: "
    equipment_position = input(
        equipment_position_prompt) or data['equipment_position']
    type_prompt = f"Bitte Typ eingeben [{data['type']}]: "
    item_type = input(type_prompt) or data['type']
    return {
        "callnumber": callnumber,
        "equipment_position": equipment_position,
        "type": item_type
    }


def get_wish() -> int:
    """ask for the action to do"""
    print_menu()
    return int(input("Ihre Wahl als Zahl: "))


def read_file() -> list:
    with open('/Users/elisabetrank/Documents/Python3/verteilerliste.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


def safe_file(data: list) -> None:
    with open('/Users/elisabetrank/Documents/Python3/verteilerliste.json', 'w', encoding='utf8') as f:
        json.dump(data, f)


datalist = [
    {
        "callnumber": "12345",
        "equipment_position": "links",
        "type": "Phone"
    },
    {
        "callnumber": "481012",
        "equipment_position": "rechts",
        "type": "Pager"
    },
    {
        "callnumber": "998776",
        "equipment_position": "top",
        "type": "Mobile"
    }
]
datalist = read_file()

print_datalist(datalist)

while True:
    wish = get_wish()

    if wish == 1:
        pos = find_item_number(datalist)
        datalist.pop(pos)
    elif wish == 2:
        pos = find_item_number(datalist)
        new_item = get_changed_item(datalist[pos])
        datalist.pop(pos)
        datalist.insert(pos, new_item)
    elif wish == 3:
        new_item = get_new_item()
        datalist.append(new_item)
    elif wish == 4:
        print_founded(datalist)
    elif wish == 5:
        print_datalist(datalist)
    elif wish == 6:
        safe_file(datalist)
    else:
        break

print_datalist(datalist)
