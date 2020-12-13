from tuples import vector
from intersection import Intersection
from shape import Shape


class Plane(Shape):
    EPSILON = 0.00001

    def __init__(self):
        Shape.__init__(self)

    def local_intersect(self, local_ray):
        if abs(local_ray.direction[1]) < self.EPSILON:
            return []

        t = -local_ray.origin[1] / local_ray.direction[1]
        return [Intersection(t, self)]

    def local_normal_at(self, local_point):
        return vector(0, 1, 0)
