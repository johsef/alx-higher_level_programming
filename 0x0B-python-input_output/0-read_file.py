#!/usr/bin/python3
"""File reader function"""


def read_file(filename=""):
    """A function that reads a text file in UTF-8 and
    prints it to stdout
    """
    with open(filename, encoding='utf-8') as my_file:
        print(my_file.read())
