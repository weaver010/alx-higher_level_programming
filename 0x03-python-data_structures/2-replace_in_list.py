#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx < 0 or idx > len(my_list):
            break
        else:
            my_list[i] = element
            break
    return(my_list)
