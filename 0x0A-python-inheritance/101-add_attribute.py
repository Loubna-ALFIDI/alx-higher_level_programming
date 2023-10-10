#!/usr/bin/python3
"""add_attribute"""


def add_attribute(obj, name, value):
    """add_attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
