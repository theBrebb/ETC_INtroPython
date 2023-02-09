#!/usr/bin/env python3
import random
"""Eine kleine "Lotto Simulation" """

"""Schreiben einen Tipp, generieren eine Ziehung und schauen ob gewonnen"""

tip = frozenset((1, 2, 3, 4, 5, 6))
ziehung = frozenset((random.sample(range(1, 46), 6)))
# print(ziehung)
hit = len(tip & ziehung)

# print(f"Tipp: {' '.join(map(str,tip))}")
# print(f"Ziehung: {' '.join(map(str,ziehung))}")

print(f" Tipp: {' '.join(map(lambda _: str(f'{_: >2d}'),sorted(tip) ))}")
print(
    f" Ziehung: {' '.join(map(lambda _: str(f'{_: >2d}'),sorted(ziehung) ))}")
print(f"Sie haben {hit=} richtige Zahlen")
