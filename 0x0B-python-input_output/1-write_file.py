#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """ writes a text file """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
