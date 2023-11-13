#!/usr/bin/python3
"""this module is on class rectangle that inherit from Base"""
from models.base import Base


class Rectangle(Base):
    """this class rectangle is a child class of Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the init method of class rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
    
    @property
    def width(self):
        """this method get the attibute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """this method set the attribute width"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be > 0".format(value))
        self.__width = value

    @property
    def height(self):
        """this method get the attribute for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """this method set the attribute for height"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be > 0".format(value))
        self.__height = value

    @property
    def x(self):
        """this method get attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """this method set attribute x"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(value))
        self.__x = value

    @property
    def y(self):
        """this method get the attribute y"""
        return (self.__y)
    @y.setter
    def y(self, value):
        """this methoe set the attribute y"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(value))
        self.__y = value

    def area(self):
        """this method returns the area value of the
        Rectangle instance."""
        return (self.width * self.height)

    def display(self):
        """this method print the instance of triangle
        with character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for z in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for k in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """this method assign an arguement to each attributes
        id, width, height, x and y"""
        if args:
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

        elif kwargs:
            if kwargs.get("id") is not None:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    
    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
