#!/usr/bin/python3
""" Peak """

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if list_of_integers:
        l = 0
        r = len(list_of_integers) - 1
        while l < r:
            m = (l + r) // 2
            if list_of_integers[m] > list_of_integers[m + 1]:
                r = m
            else:
                l = m + 1
        return list_of_integers[l]
    return None
