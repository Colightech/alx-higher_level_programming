#!/usr/bin/python3
"""a module for a new class base"""
import json


class Base:
    """the base class for other class in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """the init method for the base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """A static method that return JSON string representation
        of a dictionary"""
        if len(list_dictionaries) is None or len(list_dictionaries) == "":
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
