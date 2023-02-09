#!/usr/bin/env python3

from functools import cache
import locale

# locale.setlocale(locale.LC_NUMERIC, "")


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def main():
    for i in range(1, 501):
        print(f"{i}:\t{fib(i):n}")
    print("done")


if __name__ == "__main__":
    main()
