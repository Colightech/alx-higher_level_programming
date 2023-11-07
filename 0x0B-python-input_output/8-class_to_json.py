#!/usr/bin/python3
"""this module return  the dictionary description with
simple data structure (list, dictionary, string, intege
r and boolean) for JSON serialization of an object:"""


def class_to_json(obj):
    """the module method"""
    return obj.__dict__
