#!/usr/bin/python3
def print_last_digit(number):
    l=abs(number)%10
    print(f"{l:d}", end="")
    return(l)
