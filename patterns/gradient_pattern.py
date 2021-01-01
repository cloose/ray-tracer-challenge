from math import floor
from core import color, add, subtract, multiply, transform_from_yaml
from .pattern import Pattern


class GradientPattern(Pattern):
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
        distance = subtract(self.color_b, self.color_a)
        fraction = point[0] - floor(point[0])
        return add(self.color_a, multiply(distance, fraction))
