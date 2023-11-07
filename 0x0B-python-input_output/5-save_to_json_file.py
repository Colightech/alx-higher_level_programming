#!/usr/bin/python3
"""this module writes an Object to a text file,
using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """the method that writes an Object to a text file,
    using a JSON representation:"""
    json_out = json.dumps(my_obj)
    with open(filename, "w") as wf:
        output = wf.write(json_out)
        return (output)
