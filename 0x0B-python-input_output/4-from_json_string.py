#!/usr/bin/python3
"""this module returns an object (Python data structure)
represented by a JSON string:"""
import json


def from_json_string(my_str):
    """the module method"""
    return (json.loads(my_str))
