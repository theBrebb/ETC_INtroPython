#!urs/bin/env python3

"""Beispiel von closures, closures können Klassen ersetzen"""


def blub(x) -> callable:
    """The blubb function"""

    def inc():
        """dummy increment"""
        nonlocal x
        x = x + 1

    def dec():
        """dummy decrement"""
        nonlocal x
        x = x - 1

    def val():
        """dummy val"""
        return x
    return inc, dec, val


my_inc, my_dec, my_val = blub(3)
my_inc2, my_dec2, my_val2 = blub(3)

my_inc2()
my_inc2()
my_inc2()
my_inc2()
my_inc2()
print(my_val2())

my_inc()
my_inc()
print(my_val())
