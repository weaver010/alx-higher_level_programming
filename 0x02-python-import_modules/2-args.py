#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))
    for u in range(i):
        print("{:d}: {:s}".format(u + 1, argv[u + 1]))
