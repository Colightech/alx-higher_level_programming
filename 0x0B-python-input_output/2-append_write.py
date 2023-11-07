#!/usr/bin/python3
"""this module append a string at the edn of a text file"""


def append_write(filename="", text=""):
    """the methos to append a string at the of a text file"""
    with open(filename, "a", encoding="utf-8") as af:
        output = af.write(text)
        return (output)
