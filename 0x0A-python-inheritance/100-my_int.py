#!/usr/bin/python3
"""a module on  class MyInt that inherits from int:"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, value):
        """override == with !="""
        return self.real != value

    def __ne__(self, value):
        """override != with =="""
        return self.real == value
