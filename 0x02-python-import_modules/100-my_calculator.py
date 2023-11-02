#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    o = argv[2]
    if o != "+" and o != "-" and o != "/" and o != "*":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    if o == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif o == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif o == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
