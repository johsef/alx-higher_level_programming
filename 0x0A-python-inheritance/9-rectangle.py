#!/usr/bin/python3
"""Derived class definition"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiation of Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return(self.__width * self.__height)

    def __str__(self):
        """Prints user defined string"""
        return("[{}] {}/{}".format(
            type(self).__name__, self.__width, self.__height))
