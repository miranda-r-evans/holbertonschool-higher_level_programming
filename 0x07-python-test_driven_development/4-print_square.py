#!/usr/bin/python3


def print_square(size):
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for row in range(size):
            for col in range(size):
                print('#', end='')
            print()
