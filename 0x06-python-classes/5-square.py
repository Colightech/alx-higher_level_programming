#!/usr/bin/python3
"""a class Square that defines a square """


class Square:

    """init method"""
    def __init__(self, size=0):

        self.size = size

    """retrieve the size"""
    @property
    def size(self):
        return (self.__size)

    """set the value of the square size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """to  returns the current square area"""
    def area(self):
        return (self.__size * self.__size)

    """prints in stdout the square with the character #"""
    def my_print(self):
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
