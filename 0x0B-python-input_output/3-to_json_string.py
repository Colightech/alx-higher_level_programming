#!/usr/bin/python3
"""this module returns json representation of an object string"""
import json


def to_json_string(my_obj):
    """the module method"""
    return (json.dumps(my_obj))
