#!/usr/bin/python3
''' module containing function to check if an object inherited from another
class, excluding the class the instance was created from '''


def inherits_from(obj, a_class):
    ''' checks if an obj is an inherits from a class '''
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
