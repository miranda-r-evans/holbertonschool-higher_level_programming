#!/usr/bin/python3
''' unit testing for base class '''

import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    ''' class for testing Base '''

    def test_id_None(self):
        ''' method testing Base instance with init parameter None '''
        a = Base()
        self.assertEqual(a.id, 1)

    def test_id_int(self):
        ''' method testing Base instance with init parameter not None '''
        b = Base(57)
        self.assertEqual(b.id, 57)


    def test_id_mutable(self):
        ''' method testing for bad id values '''
        with self.assertRaises(TypeError):
            c = Base([1, 2, 3])

if __name__ == '__main__':
    unittest.main()
