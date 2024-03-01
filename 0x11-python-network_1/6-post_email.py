#!/usr/bin/python3
""" script that takes in a URL and an email address, sends a POST
"""
import sys
import requests


if __name__ == "__main__":
    f = sys.argv[1]
    s = {"email": sys.argv[2]}

    c = requests.post(f, data=s)
    print(c.text)
