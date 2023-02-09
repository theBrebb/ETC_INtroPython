#!/usr/bin/env python3

# Listen
n = ["Hallo", "Welt", 42]
print(type(n))
print(repr(n))
print(str(n))

print(n[1])
n[0] = "hello"

print(n)

n.append(50)
print(n)

g = [n[0]]
print(g)

# Tupel - sind nur lesbar
o = ("Hello", "World", 42)
print(type(o), o)

# Set - nicht indizierte Liste, nur unique list, man kann zB ne Liste auf ein Set casten um alle unique Werte zu bekommen
p = {"Hallo", "Welt", 42}
print(type(p))
print(p)
p.add(43)
p.add(43)
print(p)

# frozen Set
q = frozenset(["Hallo", "Welt", 42])
print(type(q))
print(q)

# dictionary, man kann eigentlich alles als Key verwenden, selbst None oder True

r = {
    "Question": "Warum",
    "Place": "Galaxy",
    "Answer": 42,
    None: 32
}

print(r)
Place = r[None]
print(Place)

# list comprehension, kann man nur mit Listen machen
list_upper = ([chr(x) for x in range(65, 91)])  # von 65 vis 91
list_lower = ([chr(x) for x in range(97, 123)])
list_lower_new = [y.lower() for y in list_upper]


print(list_upper)
print(list_lower)
print(list_lower_new)
