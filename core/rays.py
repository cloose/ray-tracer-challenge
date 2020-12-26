from .tuples import add, multiply
from .matrix import multiply_tuple


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def position_at(self, t):
        return add(self.origin, multiply(self.direction, t))

    def transformed(self, matrix):
        origin = multiply_tuple(matrix, self.origin)
        direction = multiply_tuple(matrix, self.direction)
        return Ray(origin, direction)
