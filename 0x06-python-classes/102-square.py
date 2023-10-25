#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    def __init__(self, size=0):
        self.__size = size

    """retriev the size of the square"""
    @property
    def size(self):
        return self.__size
    
    """set the size of the square"""
    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    """ returns the current square area"""
    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        if isinstance(other, Square):
            return self.area() == other.area()
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Square):
            return self.area() <= other.area()
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Square):
            return self.area() >= other.area()
        else:
            return False
