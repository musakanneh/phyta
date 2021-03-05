#!/usr/bin/python3

import unittest
from math import pi

from circle import circle_area


class TestCircleArea(unittest.TestCase):
    """Tests circle function"""

    def test_area(self):
        """Tests for import errors"""
        self.assertAlmostEqual(circle_area(0), pi)
