#!/usr/bin/python3
"""a module that defines a rectangle """


class Rectangle:
    """a class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """class init method"""

        self.width = width
        self.height = height

    @property
    def width(self):
        return (self__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectan = []
        for x in range(self.__height):
            [rectan.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                rectan.append("\n")
        return ("".join(rectan))
