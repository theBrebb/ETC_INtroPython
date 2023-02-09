#!/usr/bin/env python3
""" Einige Beispiele rund um Funktionen in Python"""


def print_hallo() -> None:
    """simple print hallo welt
    Input required: text to be greeted
    Output: None
    """
    print("hallo Welt")


print_hallo()


def print_string(myStr: str):
    """_summary_

    Arguments:
        myStr -- _description_

    Returns:
        _description_
    """

    print("Text: ", myStr)
    return "hallo" + myStr


def print_pass():
    pass


def s(): return print("Hallo Welt")


def my_string(*s) -> None:
    print(type(s))


my_string([1, 2, 3])


def my_info(**s) -> None:
    print(type(s))


my_info(a="b", b="c", c=1, d=[2, 4, 6])


def my_example(*s: tuple[int], **t) -> None:
    print(f"{type(s)}: {s=}")
    print(f"{type(t)}: {t=}")


my_example(1, 2, 34, a=42)

# Arbeiten mit globalen Variablen

a = 100
b = 200
c = 300


def var_function():
    global a
    a = 42
    b = 43
    print("inside function", a, b, c)


var_function()
print("outside function", a, b, c)


def named_typed_defaults_paras(a: int, b: int, c: int = 1) -> str:
    """_summary_

    Arguments:
        a -- _description_
        b -- _description_

    Keyword Arguments:
        c -- _description_ (default: {1})

    Returns:
        _description_
    """
    print(a, b, c)
    return "Hallo Welt"
