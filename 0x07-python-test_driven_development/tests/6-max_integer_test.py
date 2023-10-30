#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):


    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_greater(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
    
    def test_neg(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5, -6, -7, -8, -9]), -1)
    
    def test_middle(self):
        self.assertEqual(max_integer([1, 2, 7, 3, 4]), 7)


if __name__ == '__main__':
    unittest.main()
