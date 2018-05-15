#!/usr/bin/python3
''' module containing wrapper for type '''


def is_same_class(obj, a_class):
    ''' checks if an obj is an instance of a class '''
    if type(obj) is a_class:
        return True
    return False
