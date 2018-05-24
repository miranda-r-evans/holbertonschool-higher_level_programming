#!/usr/bin/python3
''' module for rectangle class '''

from models.base import Base


class Rectangle(Base):
    ''' rectangle class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' initializer for rectangle '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        ''' printable string of rectangle '''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter '''
        Rectangle.is_int('width', value)
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter '''
        Rectangle.is_int('height', value)
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x setter '''
        Rectangle.is_int('x', value)
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        ''' y setter '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y getter '''
        Rectangle.is_int('y', value)
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    @staticmethod
    def is_int(name='', n=0):
        ''' checks if an input is an int '''
        if type(n) is not int:
            raise TypeError('{} must be an integer'.format(name))

    def area(self):
        ''' returns area of rectangle '''
        return self.height * self.width

    def display(self):
        ''' visually displays rectangle '''
        if self.area == 0:
            return
        print('\n' * self.y +
              (' ' * self.x + '#' * self.width + '\n') * self.height, end='')

    def update(self, *args, **kwargs):
        ''' updates a rectangle with a dict's values '''
        if len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass

    def to_dictionary(self):
        ''' dict version of a rectangle '''
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    @classmethod
    def create(cls, **dictionary):
        ''' method to create a rectangle from a dict '''
        my_inst = cls(1, 1)
        my_inst.update(**dictionary)
        return my_inst
