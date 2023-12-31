#!/usr/bin/python3
"""add agr to list"""
from sys import argv


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

try:
    s = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    s = []

for i in argv[1:]:
    s.append(i)

save_file(s, 'add_item.json')
