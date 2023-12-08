#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""
    new_dict = {}
    for i, j in a_dictionary.items():
        new_dict[i] = j *2
    return (new_dict)
