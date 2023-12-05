#!/usr/bin/python3
"""write-file"""


def write_file(filename="", text=""):
    """Writes-file
    """
    with open(filename, "w", encoding="utf-8") as e:
        return e.write(text)
