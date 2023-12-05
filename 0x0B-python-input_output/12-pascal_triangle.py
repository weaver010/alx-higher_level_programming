#!/usr/bin/python3
"""Pascal"""


def pascal_triangle(n):
    """Pascal Triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    s = [[1]]
    for i in range(n - 1):
        s.append([x + n for x, n in zip(
                                        s[-1] + [0], [0] + s[-1])])
    return (s)
