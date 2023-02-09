#!/usr/bin/env/ python3

i: int = 42  # benennung von type wird derzei nicht verwendet, ändert auch nix an dem type
j: str = "42"

print(type(i))
print(type(j))

# Cast um int zu bekommen
# funktioneirt nur mit Zahlen!! Kann verwendet werden um zu überprüfen ob die Eingabe ein int ist
print(type(int(j)))

print(j)

print(type(i), ":", i)  # zeigt zype und dann die Zahl

# float
k = 42.901
l = 42.00

# cast in int schmeisst Nachkommastellen weg (nicht ab oder aufrunden)
print(type(int(k)))
print(type(l))

m = "Hello World"
print(type(m), ":", m)

# Boolean
r = True
f = False

print(type(r))
print(str(r))
# bool is immer True ausser wenn Bool == 0 oder leere Zeichenkette oder None!!
print(bool(-3))
print(bool(""))
print(bool(None))
print(bool("hallo"))

s = "Hallo Welt"
print(len(s))

print(s[-1])
print(s[0:5])  # anfang "0" is mit drin, 5. Stelle nicht (minus 1!!)

print(list(range(-10, 10, 2)))

print(list(s))
print("".join(list(s)))

# interaktive abfragen liefern immer einen str zurück, muss in int konvertieren wenn ich ne Zahl weiterverwenden will.
t = int(input("Der gewünschte Wert: "))
print(type(t), ":", t)
