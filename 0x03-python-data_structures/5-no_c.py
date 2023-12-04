#!/usr/bin/python3
def no_c(my_string):
    """Remove all c and C chars from a string"""
    new_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch
    return(new_string)
