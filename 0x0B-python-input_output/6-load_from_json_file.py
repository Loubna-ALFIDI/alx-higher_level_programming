#!/usr/bin/python3
""" load_from_json_file module """
import json


def load_from_json_file(filename):
    """ Load data from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
