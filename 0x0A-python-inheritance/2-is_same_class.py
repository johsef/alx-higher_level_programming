#!/usr/bin/python3
"""Module definition"""

def is_same_class(obj, a_class):
    """A function that returns True if the object is exactly an
    instance of the specified class or otherwise
    """
    if (type(obj) == a_class):
        return True
    return False

