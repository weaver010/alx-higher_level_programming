#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    s=[]
    for i in range(len(my_list)):
        if idx < 0 or idx > len(my_list) - 1:
            return (my_list)
        elif i != idx:
            s.append(my_list[i])
    return s
