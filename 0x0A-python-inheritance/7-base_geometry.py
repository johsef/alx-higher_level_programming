#!/usr/bin/python3
"""Defines empty class"""


class BaseGeometry():
    """A Base Geometry class
    """

    def area(self):
        """Method that raises an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates an integer"""
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
