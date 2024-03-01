#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    f = sys.argv[1]
    s = {"email": sys.argv[2]}
    a = urllib.parse.urlencode(s).encode("ascii")

    request = urllib.request.Request(f, a)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
