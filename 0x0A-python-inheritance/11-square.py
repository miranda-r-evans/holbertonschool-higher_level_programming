#!/usr/bin/python3
''' module containing a rectangle class which inherits from rectangle'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' a square class which inherits from rectangle'''

    def __init__(self, size):
        ''' initializer for square '''
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        ''' printable string of square '''
        return '[Square] {}/{}'.format(self.__size, self.__size)
