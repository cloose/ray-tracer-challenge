from math import floor, sqrt
from tuples import color, add, subtract, multiply
from matrix import identity_matrix, multiply_tuple, inverse


class Pattern:
    """Abstract base class for all patterns."""
    def __init__(self):
        self.__transform = identity_matrix()
        self.__inverse_transform = identity_matrix()

    def set_transform(self, transformation_matrix):
        """set transformation matrix for the shape"""
        self.__transform = transformation_matrix
        self.__inverse_transform = inverse(transformation_matrix)

    def transform(self):
        return self.__transform

    def inverse_transform(self):
        return self.__inverse_transform

    def pattern_at_shape(self, shape, point):
        """"""
        shape_point = multiply_tuple(shape.inverse_transform(), point)
        pattern_point = multiply_tuple(self.__inverse_transform, shape_point)
        return self.pattern_at(pattern_point)

    def pattern_at(self, point):
        raise NotImplementedError('subclass must override pattern_at')


class StripePattern(Pattern):
    """"""
    def __init__(self, color_a, color_b):
        """"""
        super().__init__()
        self.color_a = color_a
        self.color_b = color_b

    def pattern_at(self, point):
        """"""
        if floor(point[0]) % 2 == 0.0:
            return self.color_a

        return self.color_b


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


class CheckersPattern(Pattern):
    """"""
    def __init__(self, color_a, color_b):
        """"""
        super().__init__()
        self.color_a = color_a
        self.color_b = color_b

    def pattern_at(self, point):
        """"""
        if (floor(point[0]) + floor(point[1]) + floor(point[2])) % 2 == 0.0:
            return self.color_a

        return self.color_b
