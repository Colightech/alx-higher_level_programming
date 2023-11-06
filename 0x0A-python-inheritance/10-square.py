#!/usr/bin/python3
"""this module is on class Square that inherits from Rectangle01~"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle"""

    def __init__(self, size):
        """the clsaa init method"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """the area method return the product of size"""
        return self.__size*self.__size

    def __str__(self):
        """the string method return the size rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
