#!/usr/bin/python3
""" Status """
import requests

if __name__ == "__main__":
    """ Main Function """
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    data = res.text
    res_type = type(data)
    print("Body response:")
    print("\t- type: {}".format(res_type))
    print("\t- content: {}".format(data))
