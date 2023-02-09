#!/usr/bin/env python3

# printf .. "formatierte" strings, um zu strukturieren

print("\t Hallo Welt", ":", "Hello world", sep="_", end="!\n\n")
print("\t" + "Hallo Welt" + ":" + "Hello world")

i = 20
# fügt automatisch Leerzeichen ein (Separator!)
print("Ich bin", i, "Jahre alt")
# fügt keine Leerzeichen ein, muss man selbst!
print("Ich bin " + str(i) + " Jahre alt")

# leerzeichen zwischen nummer und einheit wird eingefügt (nicht optimal)
print("Ich laufe", i, "km")
print("Ich laufe " + str(i) + "km")  # umwandlung in str is nicht optimal
hello_e = "Hello world"
# deprecated variante, wird irgendwann rausfliegen also sollte man nicht verwenden
print("Hallo Welt: %s" % (hello_e))

# ab python 3.6:
print(f"Hallo Welt: {hello_e}")
# oder
print("Hallo Welt: {}".format(hello_e))
# oder
print("{wg}: {we}".format(wg='Hallo Welt', we=hello_e))
# oder
print("{1}: {0}".format('Hallo Welt', hello_e))

hallo = f"Hallo Welt: {hello_e}"

hallo = f"{'Hallo Welt': <20s}: {hello_e: >20s}"
print(hallo)
