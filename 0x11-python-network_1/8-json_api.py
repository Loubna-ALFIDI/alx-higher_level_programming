#!/usr/bin/python3
"""Search API"""
from sys import argv
import requests


if __name__ == "__main__":
    """Main function"""
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    data = {'q': q}
    res = requests.post(url, data)
    try:
        json_response = res.json()
        if 'id' in json_response and 'name' in json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON:", e)
