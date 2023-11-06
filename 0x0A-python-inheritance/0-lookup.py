#!/usr/bin/python
"""
    this module function that returns the list of available
    attributes and methods of an object:
"""


def lookup(obj):
    """a method that returns the list of available
    attributes and methods of an object:"""
    return (dir(obj))
