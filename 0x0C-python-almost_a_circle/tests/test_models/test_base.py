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


class Test_JSON(unittest.TestCase):
    ''' class for testing Base JSON methods'''

    def test_to_json_None(self):
        ''' method testing to_json input None '''
        a = Base.to_json_string(None)
        self.assertEqual(a, '[]')

    def test_to_json_empty(self):
        ''' method testing to_json input empty string '''
        b = Base.to_json_string([])
        self.assertEqual(b, '[]')

    def test_to_json_list_dict(self):
        ''' method testing to_json input valid dictionary '''
        c = Base.to_json_string([{'id': 12}])
        self.assertEqual(c, '[{"id": 12}]')

    def test_from_json_None(self):
        ''' method testing from_json input None '''
        d = Base.from_json_string(None)
        self.assertEqual(d, [])

    def test_from_json_empty(self):
        ''' method testing from_json input [] '''
        e = Base.from_json_string('[]')
        self.assertEqual(e, [])

    def test_from_json_list_dict(self):
        ''' method testing from_json input valid dictionary '''
        f = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(f, [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
