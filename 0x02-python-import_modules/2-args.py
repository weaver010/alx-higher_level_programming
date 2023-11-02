#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = len(sys.argv) - 1
    if i == 0:
        print("0 argument.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(i))
    for u in range(i):
        print("{}: {}".format(u + 1, sys.argv[u+1]))
