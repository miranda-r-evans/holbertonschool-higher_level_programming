#!/usr/bin/python3
''' module containing rectangle class '''


class Rectangle:
    ''' rectangle class with width and height '''
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
                raise TypeError('width must be an integer')
        if value < 0:
                raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
            return self.height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
                raise TypeError('height must be an integer')
        if value < 0:
                raise ValueError('height must be >= 0')
        self.__height = value
