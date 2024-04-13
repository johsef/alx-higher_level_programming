#!/usr/bin/python3
"""Append to file function"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text
    file and returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as my_file:
        return(my_file.write(text))
