#!/usr/bin/env python3

filename = "read_write.txt"
f = open(filename, "w")
print("Hallo Welt", file=f)

f.close()  # close sollte immer gemacht werden!

# mit dem "with" wird nach den Zeilen in "with" automatisch geschlossen!
with open(filename, "w", encoding="utf8") as g:
    for i in range(1, 10):
        print(f"Ich bin die Zeile {i} \n mit Nachschlag", file=g)
    g.write("Das Ende.........")
    g.write("ÄÖÜLß")

with open(filename, "r", encoding="utf8") as h:
    print(h.read())
# print(x)

with open(filename, "r", encoding="utf8") as i:
    for line in i:
        print(f"Zeile: {line}", end="")
