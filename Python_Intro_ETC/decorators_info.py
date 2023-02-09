#!/usr/bin/env python3

# Example 1: you can use functions as arguments
# def f1():
#     print("Called f1")


# def f2(f):
#     f()
#     print("f2")


# f2(f1)

# Example 2:a function wrapped from another function

# def f1(fn):
#     def wrapper():
#         print("Started")
#         fn()
#         print("Ended")
#     return wrapper


# @f1
# def f():
#     print("Hello")

# example call 1
# f1(f)()


# example call 2
# f = f1(f)
# f()

#

# f()

def f1(fn):
    def wrapper(*args, **kwargs):
        print("started")
        fn(*args, **kwargs)
        print("Ended")
    return wrapper


@f1
def f(arg1):
    print(arg1)


f(42)
f(43)
