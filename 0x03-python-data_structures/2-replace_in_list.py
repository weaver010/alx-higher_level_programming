#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if i == idx:
            my_list[i] = element
            break
        else:
            break
    return(my_list)
