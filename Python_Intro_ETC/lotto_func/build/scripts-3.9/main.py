#!/Library/Developer/CommandLineTools/usr/bin/python3

from lottery import lottery

tip = lottery.get_tip()
draw = lottery.get_draw()

print(f"Du hast {lottery.get_match(tip, draw)} Richtige!")

print(f"        Tipp: {' '.join(map(lambda _: str(f'{_: >2d}'),sorted(tip)))}")
print(
    f"     Ziehung: {' '.join(map(lambda _: str(f'{_: >2d}'),sorted(draw)))}")
