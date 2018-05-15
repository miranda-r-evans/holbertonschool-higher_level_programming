#!/usr/bin/python3
''' module containing a class that can raise an exception and validate a
 value '''


class BaseGeometry:
    ''' class that can raise an exception and validate a value '''

    def integer_validator(self, name, value):
        ''' function to validate a value '''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

    def area(self):
        ''' function that can raise exception '''
        raise Exception('area() is not implemented')
