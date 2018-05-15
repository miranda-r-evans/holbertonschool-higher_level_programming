#!/usr/bin/python3
''' module containing a class that can raise an exception '''


class BaseGeometry:
    ''' class that can raise an exception '''
    def area(self):
        ''' function that can raise exception '''
        raise Exception('area() is not implemented')
