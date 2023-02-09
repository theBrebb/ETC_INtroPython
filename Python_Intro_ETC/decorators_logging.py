#!/usr/bin/env python3
import os


def logger(f):
    """writes in a log file

    Arguments:
        f -- _description_

    Returns:
        _description_
    """
    from datetime import datetime

    def wrapper(*args, **kwargs):
        called_at = datetime.now
        logline = f"{f.__name__} executed at {called_at}"
        to_execute = f(*args, **kwargs)
        with open("log.txt", "a", encoding="utf8") as logfile:
            logfile.write(logline + os.linesep)
        print(logline)
        return to_execute
    return wrapper


@logger
def f1(arg1):
    print(arg1)


@logger
def f2():
    pass


@logger
def f3():
    pass


# wollen wissen wann unsre funktion aufgerufen wurde / loggen
f1(42)
f3()
f2()
