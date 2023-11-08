#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    c = 0
    for i in a:
        c += i
    return c
