#!/usr/bin/python3
""" Header """
from sys import argv
import requests


if __name__ == "__main__":
    """Main function"""
    url = argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))
