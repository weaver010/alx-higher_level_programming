#!/usr/bin/python3
"""read-file """


def read_file(filename=""):
    """Prints the file"""
    with open(filename, encoding="utf-8") as e:
        print(e.read(), end="")
