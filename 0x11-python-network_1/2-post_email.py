#!/usr/bin/python3
"""Email"""
from sys import argv
import urllib.request, urllib.parse


if __name__ == "__main__":
    """Main function"""
    url = argv[1]
    email = {'email': argv[2]}
    data = urllib.parse.urlencode(email).encode('utf-8')
    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
