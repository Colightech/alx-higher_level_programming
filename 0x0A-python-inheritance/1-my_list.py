#!/usr/bin/python3
"""this module is a class that inherit from a list"""


class MyList(list):
    """this class inherit from a list class"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
