#!/usr/bin/python3
''' module containing a rectangle class with width, height, area, __str__'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' a rectangle class with width, height, area, __str__'''

    def __init__(self, width, height):
        ''' initializer for rectangle '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' function that returns the area '''
        return self.__width * self.__height

    def __str__(self):
        ''' printable string of rectangle '''
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
