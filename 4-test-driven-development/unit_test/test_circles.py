#!/usr/bin/python3

import unittest
from math import pi
from circles import circle_area


class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)

    def test_empty_input(self):
        self.assertRaises(ValueError, circle_area, '')


if __name__ == '__main__':
    unittest.main()
