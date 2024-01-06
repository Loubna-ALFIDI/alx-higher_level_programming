#!/usr/bin/python3
"""Email"""
from sys import argv
import urllib.request, urllib.parse


if __name__ == "__main__":
    """Main function"""
    if len(argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        exit(1)

    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email)
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(argv[1]) as res:
        print(res.read().decode('utf-8'))
