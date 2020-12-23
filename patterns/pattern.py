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
