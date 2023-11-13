#!/usr/bin/python3
"""a module for class sqaure that inherit from class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """the init method of class squre"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """this method get the size of the sqaure"""
        return self.width

    @size.setter
    def size(self, value):
        """this method set the new size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square."""
        if args:
            for i, arg in enumerate(args):
                if i == 0 and arg is not None:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs:
            for k, v in kwargs.items():
                if k == "id" and v is not None:
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
