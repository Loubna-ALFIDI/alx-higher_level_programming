#!/usr/bin/python3
""" Status """
import requests

if __name__ == "__main__":
    """ Main Function """
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    
    if res.status_code == 200:
        html = res.content
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
    else:
        print(f"Error: {res.status_code}")