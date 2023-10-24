#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:

    """init method"""
    def __init__(self, size=0):

        self.size = size

        """retrieve size of square"""
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """to returns the current square area"""
        return (self.__size * self.__size)
