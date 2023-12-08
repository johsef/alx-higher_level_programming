#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if a_dictionary:
        h_value = sorted(a_dictionary.values())[-1]
        for k, v in a_dictionary.items():
            if h_value == v:
                return k
