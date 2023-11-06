#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    s = len(my_list) - 1
    for i in range(len(my_list)):
        if idx < 0 or idx > s:
            return(my_list)
        elif i == idx:
            my_list[i] = element
            return(my_list)
