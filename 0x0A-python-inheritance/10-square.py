#!/usr/bin/python3
"""Derived class definition"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""

    def __init__(self, size):
        """Instantiation of Square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
