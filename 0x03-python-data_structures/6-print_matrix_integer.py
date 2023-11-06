#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for u in i:
            print("{:d}".format(u),end=' ')
        print()
