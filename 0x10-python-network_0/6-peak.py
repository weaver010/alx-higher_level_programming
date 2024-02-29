#!/usr/bin/python3
"""Module finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    """
    listo = list_of_integers
    if listo == []:
        return None
    leno = len(listo)

    x, y = 0, leno - 1
    while x < y:
        z = x + (y - x) // 2
        if listo[z] > listo[z - 1] and listo[z] > listo[z + 1]:
            return listo[z]
        if listo[z - 1] > listo[z + 1]:
            y = z
        else:
            x = z + 1
    return listo[x]
