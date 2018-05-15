#!/usr/bin/python3
''' module containing wrapper for isinstance '''


def is_kind_of_class(obj, a_class):
    ''' checks if an obj is an instance of a class '''
    if isinstance(obj, a_class):
        return True
    return False
