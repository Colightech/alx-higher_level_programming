#!/usr/bin/python3
"""a module that adds a new attribute to an object if it’s possible:"""


def add_attribute(obj, att, value):
    """this method Add a new attribute to an object if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
