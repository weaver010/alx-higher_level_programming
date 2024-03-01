#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
"""
import sys
import urllib.request


if __name__ == "__main__":
    f = sys.argv[1]

    d = urllib.request.Request(f)
    with urllib.request.urlopen(d) as s:
        print(dict(s.headers).get("X-Request-Id"))
