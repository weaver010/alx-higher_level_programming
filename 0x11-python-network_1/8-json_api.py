#!/usr/bin/python3
"""
 script that takes in a letter and sends a POST
 request to http://0.0.0.0:5000/search_user
"""
import requests
from sys import argv

if __name__ == '__main__':
    q = argv[1] if len(argv) == 2 else ""
    s = 'http://0.0.0.0:5000/search_user'
    re = requests.post(s, data={'q': q})
    try:
        d = re.json()
        id, name = d.get('id'), d.get('name')
        if len(d) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(d.get('id'), d.get('name')))
    except Exception:
        print("Not a valid JSON")
