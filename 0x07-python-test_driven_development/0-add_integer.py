#!/usr/bin/python3


def add_integer(a, b=98):
    if type(a) != float and type(a) != int:
        raise TypeError('a must be an integer')
    elif type(b) != float and type(b) != int:
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
