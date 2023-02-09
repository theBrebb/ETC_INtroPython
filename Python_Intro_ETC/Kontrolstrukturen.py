
s = "Hallo Welt "

for w in s:
    print(w)

for i in range(0, len(s)):
    print(s[i])

for _ in range(0, len(s)):
    print(s[_])

if len(s) > 10:
    print("Mehr als zehn zeichen")
elif len(s) > 5:
    print("mehr als 5 zeichen aber weniger als 10")
else:
    print("Zu wenig Zeichen ")

len10 = len(s) > 10 and True or False
len10 = True if len(s) > 10 else False

# {10:05} schreibt "länger als 10" in 5 Zeichen, vorne gefüllt mit 0.
# s:_^20  _ füller, ^zentrieren, 20 Zeichen insgesammt.
if len10:
    print(
        f"Die Zeichenkette ist länger als {10:05} Zeichen und sie lautet {s:_^20}")

i = 0
while i > len(s):
    print(s[i])
    i += 1
else:
    print("Das Ende der Zeichenkette")
