#!/usr/bin/python3
"""add agr to list"""
from sys import argv


load_j = __import__('6-load_from_json_file').load_from_json_file
save_j = __import__('5-save_to_json_file').save_to_json_file

try:
    json_list = load_j('add_item.json')
except (ValueError, FileNotFoundError):
    s = []

for i in argv[1:]:
    s.append(i)

save_file(s, 'add_item.json')
