#!/usr/bin/python3
''' module for testing rectangle '''

import unittest
import sys
from io import TextIOWrapper, BytesIO
from models.base import Base
from models.rectangle import Rectangle


def setUpStdout():
    ''' function to redirect stdout to check printing '''
    old_stdout = sys.stdout
    sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)
    return old_stdout


def tearDownStdout(old_stdout):
    ''' function to reset stdout after check '''
    sys.stdout.seek(0)
    output = sys.stdout.read()
    sys.stdout.close()
    sys.stdout = old_stdout
    return output


class Test_Rect(unittest.TestCase):
    ''' class for testing Rectangle '''

    def test_init_valid(self):
        ''' tests basic initializing '''
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 4)
        self.assertEqual(a.id, 5)

    def test_bad_type(self):
        ''' tests wrong type input '''
        with self.assertRaises(TypeError):
            b = Rectangle(True, 1)

    def test_bad_int_width(self):
        ''' tests width/height value error '''
        with self.assertRaises(ValueError):
            c = Rectangle(0, 1)

    def test_bad_int_x(self):
        ''' tests x/y value error '''
        with self.assertRaises(ValueError):
            d = Rectangle(1, 1, -1)

    def test_area(self):
        ''' tests area '''
        e = Rectangle(2, 10)
        self.assertEqual(e.area(), 20)

    def test_display(self):
        ''' tests display '''
        old_stdout = setUpStdout()
        f = Rectangle(2, 3, 2, 2)
        f.display()
        self.assertEqual(tearDownStdout(old_stdout), '\n\n  ##\n  ##\n  ##\n')

    def test_print(self):
        ''' tests __str__/print '''
        old_stdout = setUpStdout()
        g = Rectangle(1, 2, 3, 4, 5)
        print(g)
        self.assertEqual(tearDownStdout(old_stdout),
                         '[Rectangle] (5) 3/4 - 1/2\n')

    def test_args_update(self):
        ''' tests update method with *args '''
        h = Rectangle(1, 2, 3, 4, 5)
        h.update(6, 7, 8, 9, 10)
        self.assertEqual(h.id, 6)
        self.assertEqual(h.width, 7)
        self.assertEqual(h.height, 8)
        self.assertEqual(h.x, 9)
        self.assertEqual(h.y, 10)

    def test_args_update_one_input(self):
        ''' tests update method to only update one attribute '''
        i = Rectangle(1, 2, 3, 4, 5)
        i.update(6)
        self.assertEqual(i.id, 6)

    def test_kwargs_update(self):
        ''' tests update method with **kwargs '''
        j = Rectangle(1, 2, 3, 4, 5)
        j.update(y=9, height=7, id=12, width=100, x=42, gafas=99)
        self.assertEqual(j.id, 12)
        self.assertEqual(j.width, 100)
        self.assertEqual(j.height, 7)
        self.assertEqual(j.x, 42)
        self.assertEqual(j.y, 9)

    def test_dictionary(self):
        ''' tests dictionary method '''
        k = Rectangle(10, 2, 1, 9, 5)
        self.assertEqual(k.to_dictionary(), {'x': 1, 'y': 9, 'id': 5,
                                             'height': 2, 'width': 10})


class Test_JSON(unittest.TestCase):
    ''' tests to make sure json methods work with rectangle '''

    def test_json(self):
        ''' tests json methods '''
        a = Rectangle(10, 7, 2, 8, 3)
        b = Rectangle(2, 4, 0, 0, 4)
        Rectangle.save_to_file([a, b])
        list_rectangles_output = Rectangle.load_from_file()
        c = list_rectangles_output[0]
        d = list_rectangles_output[1]
        self.assertEqual(a.id, c.id, 3)
        self.assertEqual(b.id, d.id, 4)
        self.assertEqual(a.width, c.width, 10)
        self.assertEqual(b.width, d.width, 2)
        self.assertEqual(a.height, c.height, 7)
        self.assertEqual(b.height, d.height, 4)
        self.assertEqual(a.x, c.x, 2)
        self.assertEqual(b.x, d.x, 0)
        self.assertEqual(a.y, c.y, 8)
        self.assertEqual(b.y, d.y, 0)


class Test_CSV(unittest.TestCase):
    ''' tests to make sure csv methods work with square '''

    def test_csv(self):
        ''' tests csv methods '''
        a = Rectangle(1, 2, 3, 4, 5)
        b = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file_csv([a, b])
        list_rectangles_output = Rectangle.load_from_file_csv()
        c = list_rectangles_output[0]
        d = list_rectangles_output[1]
        self.assertEqual(a.id, c.id, 5)
        self.assertEqual(b.id, d.id, 10)
        self.assertEqual(a.width, c.width, 1)
        self.assertEqual(b.width, d.width, 6)
        self.assertEqual(a.height, c.height, 2)
        self.assertEqual(b.height, d.height, 7)
        self.assertEqual(a.x, c.x, 3)
        self.assertEqual(b.x, d.x, 8)
        self.assertEqual(a.y, c.y, 4)
        self.assertEqual(b.y, d.y, 9)

if __name__ == '__main__':
    unittest.main()
