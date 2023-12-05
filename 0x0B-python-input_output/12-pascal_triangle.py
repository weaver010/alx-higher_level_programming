#!/usr/bin/python3
"""Pascal"""


def pascal_triangle(n):
    """Pascal Triangle
    """
    if n <= 0:
        return []

    t = [[1]]
    while len(t) != n:
        s = t[-1]
        o = [1]
        for i in range(len(s) - 1):
            o.append(tri[i] + s[i + 1])
        o.append(1)
        t.append(o)
    return t
