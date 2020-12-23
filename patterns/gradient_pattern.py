from math import floor
from core import add, subtract, multiply
from .pattern import Pattern


class GradientPattern(Pattern):
    """"""
    def __init__(self, color_a, color_b):
        """"""
        super().__init__()
        self.color_a = color_a
        self.color_b = color_b

    def pattern_at(self, point):
        distance = subtract(self.color_b, self.color_a)
        fraction = point[0] - floor(point[0])
        return add(self.color_a, multiply(distance, fraction))
