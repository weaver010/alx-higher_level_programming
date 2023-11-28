#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        order = [1, 2, 3, 4]
        self.assertEqual(max_integer(order), 4)

    def test_unordered_list(self):
        unorder = [1, 2, 11, 3]
        self.assertEqual(max_integer(unorder), 11)

    def test_max_at_begginning(self):
        max_at_first = [8, 5, 7, 1]
        self.assertEqual(max_integer(max_at_first), 8)

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        one_ele = [9]
        self.assertEqual(max_integer(one_ele), 9)

    def test_floats(self):
        floato = [5.53, 7.33, -9.123, 19.8, 6.0]
        self.assertEqual(max_integer(floato), 19.8)

    def test_ints_and_floats(self):
        ints_and_float = [5.53, 15.9, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_float), 15.9)

    def test_string(self):
        string = "xyz"
        self.assertEqual(max_integer(string), 'z')

    def test_list_of_strings(self):
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
