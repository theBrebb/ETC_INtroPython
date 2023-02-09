def fibonacci():
    """fibonacci generator
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


COUNTER = 0
for x in fibonacci():
    print(x)
    COUNTER += 1
    if COUNTER > 7:
        break
