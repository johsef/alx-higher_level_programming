#!/usr/bin/python3
"""Defining a Square class."""


class Square:
    """Represents a square with
    private attribute size.
    """

    def __init__(self, size=0):
        """Instance of a square.

        Args:
            size (int): size of square.
        """
        self.size = size

    @property
    def size(self):
        """Get current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError('size must be >=0')
        if type(value) != int:
            raise TypeError('size must be an integer')
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        return(self.size * self.size)

    def my_print(self):
        """Print the character # as area of square"""
        if self.size == 0:
            print('')
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end='')
                print()
