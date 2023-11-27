#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test for max_integer """

    def test_ord_list(self):
        """ Test Case 1: positive Ordered list """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_list(self):
        """ Test Case 2: Negative List """
        self.assertEqual(max_integer([-4, -7, -5, -1]), -1)

    def test_single_element(self):
        """ Test Case 3: Single Element """
        self.assertEqual(max_integer([5]), 5)

    def test_unord_list(self):
        """ Test Case 4: Unordered list """
        self.assertEqual(max_integer([5, 7, 8, 4]), 8)

    def test_dup_list(self):
        """ Test Case 5: Duplicate list """
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
    
    def test_ints_and_floats(self):
         """ Test Case 6: list of ints and floats """
         self.assertEqual(max_integer([1.53, 15.5, 5, -9,]), 15.5)

    def test_empty_list(self):
        """ Test Case 7: Empty list """
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
