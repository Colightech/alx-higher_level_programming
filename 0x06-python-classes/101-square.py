#!/usr/bin/python3
"""a class Square that defines a square """


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """retrieve size"""
    @property
    def size(self):
        return (self.__size)

    """to set the value of size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """this retrieve the position of the coordinate"""
    @property
    def position(self):
        return (self.__position)

    """set the vposition coordinate"""
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(count, int) for count in value) or
                not all(count >= 0 for count in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """returns the current square area"""
    def area(self):
        return (self.__size * self.__size)

    """prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for z in range(0, self.__size)]
            print("")
