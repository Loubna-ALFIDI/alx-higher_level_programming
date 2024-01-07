#!/usr/bin/python3
"""My Github"""
from sys import argv
import requests


if __name__ == "__main__":
    """Main function"""
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(argv[1], argv[2]))
    print(r.json().get('id'))
