from math import floor, sqrt
from .pattern import Pattern


class RingPattern(Pattern):
    """"""
    def __init__(self, color_a, color_b):
        """"""
        super().__init__()
        self.color_a = color_a
        self.color_b = color_b

    def pattern_at(self, point):
        """"""
        if floor(sqrt(point[0]**2 + point[2]**2)) % 2 == 0.0:
            return self.color_a

        return self.color_b
