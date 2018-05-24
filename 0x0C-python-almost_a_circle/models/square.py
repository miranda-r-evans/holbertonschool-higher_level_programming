#!/usr/bin/python3
''' module with square class '''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' square class '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' initializer for square '''
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        ''' printable version of an instance '''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        ''' size getter '''
        return self.width

    @size.setter
    def size(self, value):
        ''' size setter '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' updates a square '''
        if len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except:
                pass

    def to_dictionary(self):
        ''' dict version of a square '''
        my_dict = super().to_dictionary()
        my_dict['size'] = self.size
        del my_dict['width']
        del my_dict['height']
        return my_dict

    @classmethod
    def create(cls, **dictionary):
        ''' method to create a rectangle from a dict '''
        my_inst = cls(1)
        my_inst.update(**dictionary)
        return my_inst

    @staticmethod
    def to_csv_string(list_dictionaries):
        ''' csv string version of square '''
        if type(list_dictionaries) is not list:
            return ''
        c_str = ''
        for item in list_dictionaries:
            if type(item) is not dict:
                item = item.to_dictionary()
            c_str += str(item['id']) + ','
            c_str += str(item['size']) + ','
            c_str += str(item['x']) + ','
            c_str += str(item['y'])
            c_str += '\n'
        return c_str

    @staticmethod
    def from_csv_file(filename):
        ''' dictionary of a square from a csv '''
        new = []
        with open(filename, mode='r') as f:
            lines_of_file = f.readlines()
            for line in lines_of_file:
                line = line[:-1]
                values = line.split(',')
                my_dict = dict()
                my_dict['id'] = int(values[0])
                my_dict['size'] = int(values[1])
                my_dict['x'] = int(values[2])
                my_dict['y'] = int(values[3])
                new.append(my_dict)
        return new
