#!/usr/bin/python3
''' module containing a rectangle class with width and height'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' a rectangle class with width and height'''

    def __init__(self, width, height):
        ''' initializer for rectangle '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
