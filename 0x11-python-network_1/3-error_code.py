#!/usr/bin/python3
"""Error code"""
from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    """Main function"""
    url = argv[1]
    req = urllib.request.Request(url)
    try: urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)      

    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
