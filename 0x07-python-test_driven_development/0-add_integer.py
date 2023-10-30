#!/usr/bin/python3
"""
    add_integer: a python function that adds 2 integers.
    cast a and b into integer if any of them is
    a float and return addition of a and b
"""


def add_integer(a, b=98):

    """
        checking a and b if they are of type integer and float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
