#!/usr/bin/python3

import unittest
import sys
from io import TextIOWrapper, BytesIO
from models.square import Square


def setUpStdout():
    old_stdout = sys.stdout
    sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)
    return old_stdout

def tearDownStdout(old_stdout):
    sys.stdout.seek(0)
    output = sys.stdout.read()
    sys.stdout.close()
    sys.stdout = old_stdout
    return output

class Test_Square(unittest.TestCase):
    ''' class for testing Square '''

    def test_init_valid(self):
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.size, 1)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)
        self.assertEqual(a.id, 4)

    def test_bad_type(self):
        with self.assertRaises(TypeError):
            b = Square((1,))

    def test_bad_int_width(self):
        with self.assertRaises(ValueError):
            c = Square(0)

    def test_bad_int_x(self):
        with self.assertRaises(ValueError):
            d = Square(1, -1)

    def test_area(self):
        e = Square(5)
        self.assertEqual(e.area(), 25)

    def test_display(self):
        old_stdout = setUpStdout()
        f = Square(2, 4, 5)
        f.display()
        self.assertEqual(tearDownStdout(old_stdout), '\n\n\n\n\n    ##\n    ##\n')

    def test_print(self):
        old_stdout = setUpStdout()
        g = Square(1, 2, 3, 4)
        print(g)
        self.assertEqual(tearDownStdout(old_stdout),
                         '[Square] (4) 2/3 - 1\n')

    def test_args_update(self):
        h = Square(1, 2, 3, 4)
        h.update(6, 7, 8, 9)
        self.assertEqual(h.id, 6)
        self.assertEqual(h.size, 7)
        self.assertEqual(h.x, 8)
        self.assertEqual(h.y, 9)


    def test_args_update_one_input(self):
        i = Square(1, 2, 3, 4)
        i.update(6)
        self.assertEqual(i.id, 6)

    def test_kwargs_update(self):
        j = Square(1, 2, 3, 4)
        j.update(y=9, size=7, id=12, x=42, gafas=99)
        self.assertEqual(j.id, 12)
        self.assertEqual(j.size, 7)
        self.assertEqual(j.x, 42)
        self.assertEqual(j.y, 9)

if __name__ == '__main__':
    unittest.main()
