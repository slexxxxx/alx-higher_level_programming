#!/usr/bin/python3
"""An empty Class of Square"""


class Square:
    """Class of an empty square"""
    def __init__(self, size=0):
        """Method that initialize attributes"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that returns area of square"""
        return (self.__size**2)
