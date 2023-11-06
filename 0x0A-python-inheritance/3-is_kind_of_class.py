#!/usr/bin/python3
"""this module check if an object is an instance of class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of a class
    that inherit it"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
