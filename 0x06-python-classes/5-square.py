#!/usr/bin/python3
"""An empty Class of Square"""


class Square:
    """Class of an empty square"""

    def __init__(self, size=0):
        """Method that initialize attributes"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that returns area of square"""
        return (self.__size**2)

    def my_print(self):
        if self.size > 0:
            for x in range(self.size):
                for y in range(self.size):
                    print("#", end="")
                print()
        elif self.size == 0:
            print()
