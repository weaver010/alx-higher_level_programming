#!/usr/bin/python3

def print_square(size):
    """
    print square of #
    args:size
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
