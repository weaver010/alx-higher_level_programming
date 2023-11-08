#!/usr/bin/python3
def search_replace(my_list, search, replace):
    a = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            a.append(replace)
        else:
            a.append(my_list[i])
    return a
