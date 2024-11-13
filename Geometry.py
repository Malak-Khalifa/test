# geometry.py

import math

class Geometry:
    def __init__(self):
        pass

    def circle_circumference(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return 2 * math.pi * radius

    def rectangle_perimeter(self, length, width):
        if length < 0 or width < 0:
            raise ValueError("Length and width must be positive")
        return 2 * (length + width)
