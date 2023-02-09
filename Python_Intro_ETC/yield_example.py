#!usr/bin/env python3

"""Yields, auch bekannt unter Generator"""


def get_numberlist(max_num: int = 10) -> int:
    """return a number

    Keyword Arguments:
        max_num -- maximum number  (default: {10})

    Returns:
        returns max. num
    """
    numlist = list(range(1, max_num+1))
    for i in numlist:
        yield i


for v in get_numberlist(8):
    print(v)

print(*get_numberlist(8))
print(*get_numberlist(8))
print(*get_numberlist(8))
