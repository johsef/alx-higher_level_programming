#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples"""
    if tuple_a is None and tuple_b is None:
        return
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a += (0,)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b += (0,)

    first_t = tuple_a[0] + tuple_b[0]
    second_t = tuple_a[1] + tuple_b[1]
    return((first_t), second_t)
