#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv 
    i = len(argv) - 1
    if i == 0:
        print("0 argument.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{:d} argument:".format(i))
    for u in range(i):
        print("{:d}: {:s}".format(u + 1, argv[u + 1]))
