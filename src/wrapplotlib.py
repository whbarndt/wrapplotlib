# wrapplotlib.py
# 2022-10-04
# Making matplotlib easier to use & presentation-ready.

import matplotlib.pyplot as plt


def parent(func):
    """Example of a (parent) decorator that takes arguments."""

    def wrapper(*args, **kwargs):
        print("Parent")
        return func(*args, **kwargs)

    return wrapper


def child(func):
    """Example of a (child) decorator that takes arguments."""

    def wrapper(*args, **kwargs):
        print("Child")
        return func(*args, **kwargs)

    return wrapper


@parent
@child
def test():
    print("Hello, world.")


test()
