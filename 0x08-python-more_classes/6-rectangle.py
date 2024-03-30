#!/usr/bin/python3
"""Defining a Rectangle class."""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes rectangle with with and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Width of rectangle"""
        return self.__width

    @property
    def height(self):
        """Height of rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns area of rectangle with # character"""
        if self.__width == 0 or self.__height == 0:
            return('')

        rec = []
        for i in range(self.__height):
            for j in range(self.__width):
                rec.append("#")
            rec.append("\n")
        return("".join(rec))

    def __repr__(self):
        """Prints official string representation of rectangle"""
        return ("Rectangle({:d},{:d})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes instance of rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
