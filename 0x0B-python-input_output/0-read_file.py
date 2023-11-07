#!/usr/bin/python3
"""this module read a text file and display it to standard output"""


def read_file(filename=""):
    """the method that read the text file"""
    with open(filename, encoding="utf-8") as rf:
        for line in rf:
            print(line, end="")
