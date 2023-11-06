#!/usr/bin/python3
"""this module is on class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """calss basegeomentry (based on 6-base_geometry.py)"""
    def area(self):
        """this method raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this method validate value"""
        self.__name = name
        self.__value = value

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))
