#!/usr/bin/python3
"""this module write a string into a text file"""


def write_file(filename="", text=""):
    """the method that write the text into a file"""
    with open(filename, "w", encoding="utf-8") as wf:
        output = wf.write(text)
        return (output)
