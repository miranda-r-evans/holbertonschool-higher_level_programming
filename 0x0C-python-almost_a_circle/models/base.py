#!/usr/bin/python3
''' module containing base class '''

import json


class Base:
    ''' base class of a geometric shape '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' initializer for base class, sets instance id '''
        try:
            hash(id)
        except:
            raise TypeError('id must be immutable')
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' turns a list of dicts into a json string '''
        if type(list_dictionaries) is not list:
            return '[]'
        new = []
        for item in list_dictionaries:
            if type(item) is dict:
                new.append(item)
            else:
                new.append(item.to_dictionary())
        return json.dumps(new)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' saves a json string to a file '''
        with open('{}.json'.format(cls.__name__), mode='w+') as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        ''' loads a json string '''
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' creates a shape instance from a dict '''
        pass

    @classmethod
    def load_from_file(cls):
        ''' creates a list of instances from a json '''
        new = []
        try:
            with open('{}.json'.format(cls.__name__), mode='r') as f:
                json_string = f.read()
            list_dicts = cls.from_json_string(json_string)
            for item in list_dicts:
                new.append(cls.create(**item))
            return new
        except:
            return new

    @staticmethod
    def to_csv_string(list_dictionaries):
        ''' turns a list of dictionaries into a csv string '''
        if type(list_dictionaries) is not list:
            return ''
        c_str = ''
        for item in list_dictionaries:
            if type(item) is not dict:
                item = item.to_dictionary()
            c_str += str(item['id']) + ','
            c_str += str(item['width']) + ','
            c_str += str(item['height']) + ','
            c_str += str(item['x']) + ','
            c_str += str(item['y'])
            c_str += '\n'
        return c_str

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' saves a csv string to a file '''
        with open('{}.csv'.format(cls.__name__), mode='w+') as f:
            f.write(cls.to_csv_string(list_objs))

    @staticmethod
    def from_csv_file(filename):
        ''' creates a list of dicts from a csv '''
        new = []
        with open(filename, mode='r') as f:
            lines_of_file = f.readlines()
            for line in lines_of_file:
                line = line[:-1]
                values = line.split(',')
                my_dict = dict()
                my_dict['id'] = int(values[0])
                my_dict['width'] = int(values[1])
                my_dict['height'] = int(values[2])
                my_dict['x'] = int(values[3])
                my_dict['y'] = int(values[4])
                new.append(my_dict)
        return new

    @classmethod
    def load_from_file_csv(cls):
        ''' creates a list of instances from a csv '''
        new = []
        try:
            my_list = cls.from_csv_file('{}.csv'.format(cls.__name__))
            for item in my_list:
                new.append(cls.create(**item))
            return new
        except:
            return new
