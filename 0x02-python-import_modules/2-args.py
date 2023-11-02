#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    if i == 0:
        print("0 argument.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(i - 1))
    if i >= 1:
        for i in range(1, i + 1):
            print("{}: {}".format(i, sys.argv[i]))
