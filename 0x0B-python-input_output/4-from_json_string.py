#!/usr/bin/python3
"""json"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure)
    represented by a JSON string"""
    return json.loads(my_str)
