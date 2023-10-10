#!/usr/bin/python3
""" from_json_string """
import json


def from_json_string(my_str):
    """ Converts a JSON string to an object. """
    return json.loads(my_str)
