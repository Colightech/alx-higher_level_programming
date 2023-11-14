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
    @staticmethod
    def to_json_string(list_dictionaries):
        """A static method that return JSON string representation
        of a dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == "[]":
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
    @classmethod
    def save_to_file(cls, list_objs):
        """this method write the json string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as wf:
            if list_objs is None:
                wf.write("[]")
            else:
                list_dicts = [a.to_dictionary() for a in list_objs]
                wf.write(Base.to_json_string(list_dicts))
    @staticmethod
    def from_json_string(json_string):
        """this static method returns list of json string"""
        if json_string is None or len(json_string) == "[]":
            return ("[]")
        else:
            return (json.loads(json_string))

    def create(cls, **dictionary):
        """this method return an instance of a set attribute"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                temp = cls(1, 1)
            else:
                temp = cls(1)
            temp.update(**dictionary)
            return (temp)

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings."""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return ("[]")

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as rf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(rf, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in a.items())
                              for a in list_dicts]
                return [cls.create(**a) for a in list_dicts]
        except IOError:
            return ("[]")


