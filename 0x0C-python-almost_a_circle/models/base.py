#!/usr/bin/python3
"""a module for a new class base"""



class Base:
    """the base class for other class in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """the init method for the base class"""

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
