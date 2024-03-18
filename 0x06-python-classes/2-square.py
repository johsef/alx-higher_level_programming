#!/usr/bin/python3
"""Defining a Square class."""


class Square:
    """Represents a square with
    private attribute size."""
    def __init__(self, size=0):
        """Instance of a square.

        Args:
            size (int): size of square.
        """
        if size < 0:
            raise ValueError('size must be >=0')
        if type(size) != int:
            raise TypeError('size must be an integer')
        self.__size = size
