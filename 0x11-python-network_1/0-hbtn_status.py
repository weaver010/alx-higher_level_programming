#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen
    ('https://alx-intranet.hbtn.io/status') as response:
        f = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(f)))
        print("\t- content: {}".format(f))
        print("\t- utf8 content: {}".format(f.decode("UTF-8")))
