#!/usr/bin/python3

import unittest
import sys
from io import TextIOWrapper, BytesIO
from models.rectangle import Rectangle


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

class Test_Rect(unittest.TestCase):
    ''' class for testing Rectangle '''

    def test_init_valid(self):
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 4)
        self.assertEqual(a.id, 5)

    def test_bad_type(self):
        with self.assertRaises(TypeError):
            b = Rectangle(True, 1)

    def test_bad_int_width(self):
        with self.assertRaises(ValueError):
            c = Rectangle(0, 1)

    def test_bad_int_x(self):
        with self.assertRaises(ValueError):
            d = Rectangle(1, 1, -1)

    def test_area(self):
        e = Rectangle(2, 10)
        self.assertEqual(e.area(), 20)

    def test_display(self):
        old_stdout = setUpStdout()
        f = Rectangle(2, 3, 2, 2)
        f.display()
        self.assertEqual(tearDownStdout(old_stdout), '\n\n  ##\n  ##\n  ##\n')

    def test_print(self):
        old_stdout = setUpStdout()
        g = Rectangle(1, 2, 3, 4, 5)
        print(g)
        self.assertEqual(tearDownStdout(old_stdout),
                         '[Rectangle] (5) 3/4 - 1/2\n')

    def test_args_update(self):
        h = Rectangle(1, 2, 3, 4, 5)
        h.update(6, 7, 8, 9, 10)
        self.assertEqual(h.id, 6)
        self.assertEqual(h.width, 7)
        self.assertEqual(h.height, 8)
        self.assertEqual(h.x, 9)
        self.assertEqual(h.y, 10)


    def test_args_update_one_input(self):
        i = Rectangle(1, 2, 3, 4, 5)
        i.update(6)
        self.assertEqual(i.id, 6)

    def test_kwargs_update(self):
        j = Rectangle(1, 2, 3, 4, 5)
        j.update(y=9, height=7, id=12, width=100, x=42, gafas=99)
        self.assertEqual(j.id, 12)
        self.assertEqual(j.width, 100)
        self.assertEqual(j.height, 7)
        self.assertEqual(j.x, 42)
        self.assertEqual(j.y, 9)

if __name__ == '__main__':
    unittest.main()
