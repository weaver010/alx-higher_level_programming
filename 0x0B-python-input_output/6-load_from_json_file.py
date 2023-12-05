#!/usr/bin/python3
"""JSON"""
import json


def load_from_json_file(filename):
    """JSON"""
    with open(filename) as e:
        return json.load(e)
