#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    divide matrix
    arg: matrix, div
    Raises:TypeError,ZeroDivisionError
    Returns:matrix of div
    """
    row = None
    e = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(e)

    for i in matrix:
        if not i or not isinstance(i, list):
            raise TypeError(e)

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(e)

        if row is None:
            row = len(i)
        elif row != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    d_mat = [[round(j / div, 2) for j in i] for i in matrix]

    return d_mat
