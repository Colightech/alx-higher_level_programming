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
        if list_dictionaries is None or len(list_dictionaries) == "":
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    def save_to_file(cls, list_objs):
        """this method write the json string representation to a file"""
        with open("Rectangle.json", 'w') as wf:
            json_str = to_json_string(json.dump(cls, list_objs))
            wf.write(json_str)

    def from_json_string(json_string):
        """this static method returns list of json string"""
        if json_string is None or len(json_string) == 0:
            return ("[]")
        else:
            return (json.loads(json_string))
