#!/usr/bin/python3
"""File reader function"""


def write_file(filename="", text=""):
    """A function writes to a text file and return the
    number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return(my_file.write(text))
