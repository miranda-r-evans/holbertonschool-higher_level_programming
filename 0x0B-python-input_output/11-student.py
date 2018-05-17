#!/usr/bin/python3
''' module containing a class student '''
class_to_json = __import__('10-class_to_json').class_to_json


class Student():
    ''' the class student, with initializer, to_json '''
    def __init__(self, first_name, last_name, age):
        ''' initializer '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' creates a dict of instance attributes, handy for json '''
        return self.__dict__
