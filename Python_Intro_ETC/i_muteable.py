#!/usr/bin/env python3

x = 42
print(f"{x=}, Typ: {type(x)}, Id: {id(x)}")

x = 42
print(f"{x=}, Typ: {type(x)}, Id: {id(x)}")

x = 43
print(f"{x=}, Typ: {type(x)}, Id: {id(x)}")

y = 43
print(f"{y=}, Typ: {type(y)}, Id: {id(y)}")

y = 44
print(f"{y=}, Typ: {type(y)}, Id: {id(y)}")
print(f"{x=}, Typ: {type(x)}, Id: {id(x)}")

z = [1, 2, 3]
print(f"{z=}, Typ: {type(z)}, Id: {id(z)}")
z.pop()
z.append(4)
print(f"{z=}, Typ: {type(z)}, Id: {id(z)}")

a = {"a": 42, "b": 43}
print(f"{a=}, Typ: {type(a)}, Id: {id(a)}")
a.pop("a")
a["c"] = 44
print(f"{a=}, Typ: {type(a)}, Id: {id(a)}")

# WOzu
c = [1, 2, 3]
d = c
print(f"{c=} {d=}, Typ: {type(c)} {type(d)}, Id: {id(c)} {id(d)}")

d.pop()
print(f"{c=} {d=}, Typ: {type(c)} {type(d)}, Id: {id(c)} {id(d)}")

# copy hilft
c = [1, 2, 3]
d = c.copy
print(f"{c=} {d=}, Typ: {type(c)} {type(d)}, Id: {id(c)} {id(d)}")


def add_value(x, y=[1, 2, 3]):
    y.append(x)
    print(f"{y=} Id: {id(y)}")


add_value(4)
add_value(5)
add_value(6)
