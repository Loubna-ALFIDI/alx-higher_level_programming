#!/usr/bin/python3
""" read_file module """


def read_file(filename=""):
    """ reads a text file """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
