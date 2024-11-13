# test_geometry.py

import unittest
from geometry import Geometry

class TestGeometry(unittest.TestCase):

    def setUp(self):
        # This method runs before each test.
        self.geometry = Geometry()

    def test_circle_circumference(self):
        # Test the circle_circumference functionality
        result = self.geometry.circle_circumference(5)
        self.assertAlmostEqual(result, 31.41592653589793, places=5)

        result = self.geometry.circle_circumference(0)
        self.assertEqual(result, 0)

        # Test for negative radius, expecting a ValueError
        with self.assertRaises(ValueError):
            self.geometry.circle_circumference(-3)

    def test_rectangle_perimeter(self):
        # Test rectangle_perimeter functionality
        result = self.geometry.rectangle_perimeter(4, 6)
        self.assertEqual(result, 20)

        result = self.geometry.rectangle_perimeter(10, 2)
        self.assertEqual(result, 24)

        # Test for negative length or width, expecting a ValueError
        with self.assertRaises(ValueError):
            self.geometry.rectangle_perimeter(-4, 5)

        with self.assertRaises(ValueError):
            self.geometry.rectangle_perimeter(4, -5)
