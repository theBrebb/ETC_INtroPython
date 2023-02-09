#!/usr/bin/emv python3

num1 = 5
num2 = 0
calc = 0
try:
    calc = num1 / num2
except ZeroDivisionError as err:
    print(
        f"Durch Null kann nicht geteilt werden, Wert wird auf 1 gesetzt!{err=}")
    num2 = 1
    calc = num1 / num2
finally:
    print(f"{calc=}, {num1=}, {num2=}")


def my_diff(n1, n2) -> int:
    if n2 == 0:
        raise ValueError("Division durch 0 nicht möglich!")
    return n1/n2


try:
    print(my_diff(4, 2))
    print(my_diff(4, 0))
    print(my_diff(6, 3))
except ValueError as err:
    print(err)

print("ende des Programms")
