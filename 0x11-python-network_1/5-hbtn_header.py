#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
"""
import sys
import requests


if __name__ == "__main__":
    s = sys.argv[1]

    d = requests.get(s)
    print(d.headers.get("X-Request-Id"))
