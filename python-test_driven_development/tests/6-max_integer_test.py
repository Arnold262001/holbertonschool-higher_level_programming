#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular1(self):
        self.assertEqual(max_integer([4, 2]), 4)

    def test_regular2(self):
        self.assertEqual(max_integer([4, 2, 8]), 8)

    def test_regular3(self):
        self.assertEqual(max_integer([9]), 9)

    def test_list_empty(self):
        self.assertIsNone(max_integer([]), None)
