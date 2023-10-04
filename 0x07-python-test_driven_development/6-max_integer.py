#!/usr/bin/python3
"""Module 6-max_integer.py"""


def max_integer(list=[]):
    """Return the max integer in a list
    Args:
        list (list): list of integers
    Return:
        max integer in list
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
