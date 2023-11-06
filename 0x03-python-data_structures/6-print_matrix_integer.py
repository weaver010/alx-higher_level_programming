#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        s=1
        for u in i:
            if s==len(i):
                print("{:d}".format(u),end='')
            else:
                print("{:d}".format(u),end=' ')
                s+=1
        print()
