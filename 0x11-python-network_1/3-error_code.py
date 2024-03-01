#!/usr/bin/python3
""" script that takes in a URL, sends a request ...
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    f = sys.argv[1]

    d = urllib.request.Request(f)
    try:
        with urllib.request.urlopen(d) as s:
            print(s.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
