#!/usr/bin/python3
""" class_to_json module """


def class_to_json(obj):
    """Convert class to json."""
    return obj.__dict__
