#!/usr/bin/python3
"""this module  that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """the method of module"""
    txt = ''
    with open(filename, 'r') as rf:
        for line in rf:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, 'w') as wf:
        wf.write(txt)
