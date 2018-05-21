#!/usr/bin/python3
''' module for testing square '''

import unittest
import sys
from io import TextIOWrapper, BytesIO
from models.square import Square


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


class Test_Square(unittest.TestCase):
    ''' class for testing Square '''

    def test_init_valid(self):
        ''' tests basic initializing '''
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.size, 1)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)
        self.assertEqual(a.id, 4)

    def test_bad_type(self):
        ''' tests wrong type input '''
        with self.assertRaises(TypeError):
            b = Square((1,))

    def test_bad_int_size(self):
        ''' tests size value error '''
        with self.assertRaises(ValueError):
            c = Square(0)

    def test_bad_int_x(self):
        ''' tests x/y value error '''
        with self.assertRaises(ValueError):
            d = Square(1, -1)

    def test_area(self):
        ''' tests area '''
        e = Square(5)
        self.assertEqual(e.area(), 25)

    def test_display(self):
        ''' tests display '''
        old_stdout = setUpStdout()
        f = Square(2, 4, 5)
        f.display()
        self.assertEqual(tearDownStdout(old_stdout),
                         '\n\n\n\n\n    ##\n    ##\n')

    def test_print(self):
        ''' tests __str__/print '''
        old_stdout = setUpStdout()
        g = Square(1, 2, 3, 4)
        print(g)
        self.assertEqual(tearDownStdout(old_stdout),
                         '[Square] (4) 2/3 - 1\n')

    def test_args_update(self):
        ''' tests update method with *args '''
        h = Square(1, 2, 3, 4)
        h.update(6, 7, 8, 9)
        self.assertEqual(h.id, 6)
        self.assertEqual(h.size, 7)
        self.assertEqual(h.x, 8)
        self.assertEqual(h.y, 9)

    def test_args_update_one_input(self):
        ''' tests update method to only update one attribute '''
        i = Square(1, 2, 3, 4)
        i.update(6)
        self.assertEqual(i.id, 6)

    def test_kwargs_update(self):
        ''' tests update method with **kwargs '''
        j = Square(1, 2, 3, 4)
        j.update(y=9, size=7, id=12, x=42, gafas=99)
        self.assertEqual(j.id, 12)
        self.assertEqual(j.size, 7)
        self.assertEqual(j.x, 42)
        self.assertEqual(j.y, 9)

    def test_dictionary(self):
        ''' tests dictionary method '''
        h = Square(10, 2, 1, 5)
        self.assertEqual(h.to_dictionary(),
                         {'id': 5, 'x': 2, 'size': 10, 'y': 1})


class Test_JSON(unittest.TestCase):
    ''' tests to make sure json methods work with square '''

    def test_json(self):
        ''' tests json methods '''
        a = Square(10, 7, 2, 8)
        b = Square(2, 4, 0, 0)
        Square.save_to_file([a, b])
        list_s_output = Square.load_from_file()
        c = list_s_output[0]
        d = list_s_output[1]
        self.assertEqual(a.id, c.id, 8)
        self.assertEqual(b.id, d.id, 0)
        self.assertEqual(a.size, c.size, 10)
        self.assertEqual(b.size, d.size, 2)
        self.assertEqual(a.x, c.x, 7)
        self.assertEqual(b.x, d.x, 4)
        self.assertEqual(a.y, c.y, 2)
        self.assertEqual(b.y, d.y, 0)


class Test_CSV(unittest.TestCase):
    ''' tests to make sure csv methods work with square '''

    def test_csv(self):
        ''' tests csv methods '''
        a = Square(1, 2, 3, 4)
        b = Square(6, 7, 8, 9)
        Square.save_to_file_csv([a, b])
        list_s_output = Square.load_from_file_csv()
        c = list_s_output[0]
        d = list_s_output[1]
        self.assertEqual(a.id, c.id, 4)
        self.assertEqual(b.id, d.id, 9)
        self.assertEqual(a.size, c.size, 1)
        self.assertEqual(b.size, d.size, 6)
        self.assertEqual(a.x, c.x, 2)
        self.assertEqual(b.x, d.x, 7)
        self.assertEqual(a.y, c.y, 3)
        self.assertEqual(b.y, d.y, 8)

if __name__ == '__main__':
    unittest.main()
