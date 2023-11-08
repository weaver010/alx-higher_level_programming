#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = sorted(a_dictionary)
    for i in s:
        print("{:s}: {}".format(i, a_dictionary[i]))
