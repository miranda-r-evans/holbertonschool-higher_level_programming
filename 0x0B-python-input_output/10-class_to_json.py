#!usr/bin/python3
''' module with dictionary-creation function '''


def class_to_json(obj):
    ''' returns attributes of object '''
    return obj.__dict__
