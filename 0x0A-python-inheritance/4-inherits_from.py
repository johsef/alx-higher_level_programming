#!/usr/bin/python3
"""Module definition"""

def inherits_from(obj, a_class):
    """A function that returns True if the object is
    an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False.
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
