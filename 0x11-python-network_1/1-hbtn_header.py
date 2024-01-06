#!/usr/bin/python3
""" Header """
from sys import argv
import urllib.request


if __name__ == "__main__":
    """Main function"""
    with urllib.request.urlopen(argv[1]) as r:
        print(r.headers.get('X-Request-Id'))
