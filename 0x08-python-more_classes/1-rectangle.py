#!/usr/bin/python3
"""a module that define a rectangle
"""


class Rectangle:
    """class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """init instance method"""
        self.__width = width
        self.__height = height

        self.__width = width
        self.__height = height

        """method to retrieve the width"""
        @property
        def width(self):
            return (self.__width)

        """method that set the with"""
        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        """method the retrieve the height"""
        @property
        def height(self):
            return (self.__height)

        """method that set the height"""
        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
