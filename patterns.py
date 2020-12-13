from math import floor
from matrix import identity_matrix, multiply_tuple, inverse


class StripePattern:
    """"""
    def __init__(self, color_a, color_b):
        """"""
        self.color_a = color_a
        self.color_b = color_b
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

    def pattern_at(self, point):
        """"""
        if floor(point[0]) % 2 == 0.0:
            return self.color_a

        return self.color_b

    def pattern_at_shape(self, shape, point):
        """"""
        shape_point = multiply_tuple(shape.inverse_transform(), point)
        pattern_point = multiply_tuple(self.__inverse_transform, shape_point)
        return self.pattern_at(pattern_point)
