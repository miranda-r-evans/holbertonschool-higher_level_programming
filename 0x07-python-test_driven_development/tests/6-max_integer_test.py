#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-8, 3, 4]), 4)
        self.assertEqual(max_integer([5, 5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([]), )
        self.assertEqual(max_integer(), )
        self.assertEqual(max_integer('string'), 't')
        self.assertEqual(max_integer(['string1', 'string2'], 'string2')
        self.assertEqual(max_integer((1, 2)), 2)

    def test_errors(self):
        with self.assertRaises(TypeError):
            max_integer(400, 'string')
        with self.assertRaises(TypeError):
            max_integer(1)
        with self.assertRaises(TypeError):
            max_integer({3, 4})
        with self.assertRaises(KeyError):
            max_integer({'num1': 3, 'num2': 4})
