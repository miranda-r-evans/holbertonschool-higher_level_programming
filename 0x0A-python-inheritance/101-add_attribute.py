#!/usr/bin/python3
''' module containing function to add an attribure to a class '''


def add_attribute(cls_instance, att_name, att_val):
    ''' function that adds a new attribute to an instance if possible '''
    cls_name = type(cls_instance)
    if type(cls_name) is type and '__dict__' in cls_name.__dict__:
        cls_instance.__dict__[str(att_name)] = att_val
    else:
        raise TypeError("can't add new attribute")
