#!/ur/bin/env python3

import random


def get_tip() -> frozenset[int]:
    while True:
        try:
            tip = input("Ihre Zahlen: ")
            if verify_tip(tip):
                return frozenset(map(int, tip.split()))
        except ValueError:
            print("""Bitte geben Sie 6 Zahlen getrennt durch 
                  ein Leerzeichen zwischen 1 und 45 ein: """)
        except KeyboardInterrupt:
            exit()


def get_draw() -> frozenset[int]:
    return frozenset(random.sample(range(1, 46), 6))


def verify_tip(tip: str) -> bool:
    tiplist = set(tip.split())
    tiplist = set(map(int, tiplist))
    if len(tiplist) != 6:
        return False

    for _ in tiplist:
        if _ < 1 or _ > 45:
            return False

    return True


def get_match(tip: frozenset[int], draw: frozenset[int]) -> int:
    return len(tip & draw)
