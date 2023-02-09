#!/usr/bin/env python3

import csv
import os
print(os.linesep)
data = [
    {
        "name": "Peter",
        "date_of_birth": "1990-12-21",
        "address": "Stephansplatz 1, 1010 Wien"
    },
    {
        "name": "Susi",
        "date_of_birth": "1990-10-20",
        "address": "Karlsplatz 1, 1010 Wien"
    },
    {
        "name": "Hans",
        "date_of_birth": "1980-02-05",
        "address": "Schwedenplatz 1, 1010 Wien"
    },
    {
        "name": "Petra",
        "date_of_birth": "2000-04-30",
        "address": "Albertinaplatz 1, 1010 Wien"
    },
]

datadir = os.path.abspath(os.path.dirname(__file__) + "/data")
datafile = datadir + "/data.csv"
with open(datafile, "w", encoding="utf8") as csvfile:
    datawriter = csv.writer(csvfile, delimiter=";",
                            quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\n")
    for person in data:
        datawriter.writerow(
            [person["name"], person["date_of_birth"], person["address"]])


with open(datafile, "r", encoding="utf8") as csvfile:
    datareader = csv.reader(csvfile, delimiter=";",  # data reader gibt liste retour!
                            quotechar='"', lineterminator="\n")
    print(datareader)
    for person in datareader:
        print("......".join(person))

os.remove(datafile)
