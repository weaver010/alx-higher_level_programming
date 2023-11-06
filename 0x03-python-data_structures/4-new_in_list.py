#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    s = my_list[:]
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        s[idx] = element
        return s
