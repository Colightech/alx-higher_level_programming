#!/usr/bin/python3
"""thismodule load an object from json file"""
import json


def load_from_json_file(filename):
    """the module method to load an object from json file"""
    with open(filename) as rf:
        return json.load(rf)
