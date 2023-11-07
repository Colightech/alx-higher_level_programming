#!/usr/bin/python3
"""this module defines a class student on student"""


class Student:
    """module class"""
    def __init__(self, first_name, last_name, age):
        """class init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """the class public method"""
        return self.__dict__
