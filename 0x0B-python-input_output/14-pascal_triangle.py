#!/usr/bin/python3
''' module with pascal's triangle function '''


def pascal_triangle(n):
    ''' returns a multidimensional list representing a pascal's triangle
    of n size '''
    if n <= 0:
        return []
    triangle = [[1]]
    for row in range(n - 1):
        new = [1]
        for i in range(len(triangle[-1]) - 1):
            new.append(triangle[-1][i] + triangle[-1][i + 1])
        new.append(1)
        triangle.append(new)
    return triangle
