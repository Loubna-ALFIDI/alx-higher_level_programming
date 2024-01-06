#!/usr/bin/python3
"""Error code"""
from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    """Main function"""
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
