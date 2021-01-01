from math import floor
from core import color, transform_from_yaml
from .pattern import Pattern


class CheckersPattern(Pattern):
    """"""
    def __init__(self, color_a, color_b):
        """"""
        super().__init__()
        self.color_a = color_a
        self.color_b = color_b

    @classmethod
    def from_yaml(cls, data):
        pattern_data = data['pattern']

        color_a = pattern_data['colors'][0]
        color_b = pattern_data['colors'][1]
        pattern = cls(color(color_a[0], color_a[1], color_a[2]),
                      color(color_b[0], color_b[1], color_b[2]))

        if 'transform' in pattern_data:
            pattern.set_transform(transform_from_yaml(pattern_data))

        return pattern

    def pattern_at(self, point):
        """"""
        x = abs(point[0])
        y = abs(point[1])
        z = abs(point[2])
        if (floor(x) + floor(y) + floor(z)) % 2 == 0.0:
            return self.color_a

        return self.color_b
