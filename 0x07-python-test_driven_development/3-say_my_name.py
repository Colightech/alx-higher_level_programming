#!/usr/bin/python3
"""
    a function that prints My name
    and all names must be in string
"""


def say_my_name(first_name, last_name=""):
    
    """function prototyp"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
    return (first_name, last_name)
