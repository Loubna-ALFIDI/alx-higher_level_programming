#!/usr/bin/python3
""" Peak """


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if list_of_integers:
        left_side = 0
        right_side = len(list_of_integers) - 1
        while left_side < right_side:
            m = (left_side + right_side) // 2
            if list_of_integers[m] > list_of_integers[m + 1]:
                right_side = m
            else:
                left_side = m + 1
        return list_of_integers[left_side]
    return None
