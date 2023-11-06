#!/usr/bin/python3
def max_integer(my_list=[]):
    s=my_list[0]
    if my_list==[]:
        return None
    else:
        for i in my_list:
            if i>s:
                s=i
        return s
