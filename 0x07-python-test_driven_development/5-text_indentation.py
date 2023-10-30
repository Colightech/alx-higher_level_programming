#!/usr/bin/python3
"""
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """function prototype"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuate = ['.', '?', ':']
    lines = []
    line = ""

    for char in text:
        line += char
        if char in punctuate:
            lines.append(line.strip())
            lines.append("")
            line = ""

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
