#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    av = 0
    al = 0
    for i in my_list:
        av += i[0] * i[1]
        al += i[1]
    return float(av / al)
