#!/usr/bin/python3
"""print_sorted"""


class MyList(list):
    """print the sorted list"""
    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
