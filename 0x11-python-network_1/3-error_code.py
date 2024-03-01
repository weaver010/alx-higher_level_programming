#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    f = sys.argv[1]

    request = urllib.request.Request(f)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
