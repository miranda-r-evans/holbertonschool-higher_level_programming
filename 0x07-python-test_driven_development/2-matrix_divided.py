#!/usr/bin/python3


def matrix_divided(matrix, div):
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0 or div == 0.0:
        raise ZeroDivisionError('division by zero')
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    rowlen = len(matrix[0])
    for row in matrix:
        if type(row) != list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(row) != rowlen:
            raise TypeError('Each row of the matrix must have the same size')
        for num in row:
            if type(num) != int and type(num) != float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    div = div
    return [[round(x / div, 2) for x in row] for row in matrix]
