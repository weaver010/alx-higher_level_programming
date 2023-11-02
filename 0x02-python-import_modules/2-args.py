#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 1:
        print("0 argument.")
    elif i == 2:
        print("1 argument:")
    else:
        print("{} argument:".format(i - 1))
    if i >= 2:
        for i in range(1, i):
            print("{}: {}".format(i, sys.argv[i]))
