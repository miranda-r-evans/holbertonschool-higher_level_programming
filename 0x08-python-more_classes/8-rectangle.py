#!/usr/bin/python3
''' module containing rectangle class '''


class Rectangle:
    ''' rectangle class with width, height, area, perimeter, string, repr,
    del message, instance counter, print symbol, and size compare '''

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances = type(self).number_of_instances + 1

    def __del__(self):
        print('Bye rectangle...')
        type(self).number_of_instances = type(self).number_of_instances - 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
                raise TypeError('width must be an integer')
        if value < 0:
                raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
            return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
                raise TypeError('height must be an integer')
        if value < 0:
                raise ValueError('height must be >= 0')
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        string = ''
        for row in range(self.__height):
            for col in range(self.__width):
                string = string + str(self.print_symbol)
            string = string + '\n'
        return string[:-1]

    def __repr__(self):
        return 'Rectangle('+str(self.__width) + ', '+str(self.__height) + ')'
