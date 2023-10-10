#!/usr/bin/python3
"""is inherits from"""


def inherits_from(obj, a_class):
    """inherits_from"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
