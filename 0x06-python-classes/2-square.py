#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:

    """Instantiation with optional size"""
    def __init__(self, size=0):

        """using a try block"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
