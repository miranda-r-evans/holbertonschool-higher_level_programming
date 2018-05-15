#!/usr/bin/python3
''' module containing MyInt class (based on int) '''


class MyInt(int):
    ''' class based on int, with == and != operators reversed '''

    def __eq__(self, other):
        ''' equality operator '''
        if int(self) == int(other):
            return False
        return True

    def __ne__(self, other):
        ''' unequality operator '''
        if int(self) == int(other):
            return True
        return False
