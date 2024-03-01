#!/usr/bin/python3
"""
 script that takes your GitHub credentials
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    s = 'https://api.github.com/users/{}'.format(argv[1])
    d = requests.get(s,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(d.json().get('id'))
