from math import floor
from .pattern import Pattern


class CheckersPattern(Pattern):
    """"""
    def __init__(self, color_a, color_b):
        """"""
        super().__init__()
        self.color_a = color_a
        self.color_b = color_b

    def pattern_at(self, point):
        """"""
        x = abs(point[0])
        y = abs(point[1])
        z = abs(point[2])
        if (floor(x) + floor(y) + floor(z)) % 2 == 0.0:
            return self.color_a

        return self.color_b
