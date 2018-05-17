#!/usr/bin/python3
''' module containing a class student '''


class Student():
    ''' the class student, with initializer, to_json '''
    def __init__(self, first_name, last_name, age):
        ''' initializer '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' creates a dict of instance attributes, handy for json '''
        if isinstance(attrs, list) is True:
            my_dict = dict()
            for key in attrs:
                if key in self.__dict__:
                    my_dict[key] = self.__dict__[key]
            return my_dict
        return self.__dict__
