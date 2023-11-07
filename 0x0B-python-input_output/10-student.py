#!/usr/bin/python3
"""this module defines a class student on student"""


class Student:
    """module class"""
    def __init__(self, first_name, last_name, age):
        """class init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """the class public method"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
