#!/usr/bin/python3
"""Defines new class"""


class MyList(list):
    """A class that inherits from list class
    """

    def print_sorted(self):
        """Method that prints sorted list"""
        print(sorted(self))
