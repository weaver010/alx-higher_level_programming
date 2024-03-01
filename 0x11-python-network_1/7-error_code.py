#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
"""
import requests
from sys import argv

if __name__ == '__main__':
    f = requests.get(argv[1])
    s = f.status_code
    print(f.text) if s < 400 else print(
        "Error code: {}".format(f.status_code))
