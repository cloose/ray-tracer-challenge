from math import inf
from tuples import vector
from material import Material
from intersection import Intersection
from transformations import transform_from_yaml
from .shape import Shape


class Cube(Shape):
    EPSILON = 0.00001

    def __init__(self):
        super().__init__()

    @classmethod
    def from_yaml(cls, data):
        cube = cls()

        if 'transform' in data:
            cube.set_transform(transform_from_yaml(data))

        if 'material' in data:
            cube.material = Material.from_yaml(data)

        return cube

    def local_intersect(self, local_ray):
        xtmin, xtmax = self.check_axis(local_ray.origin[0],
                                       local_ray.direction[0])
        ytmin, ytmax = self.check_axis(local_ray.origin[1],
                                       local_ray.direction[1])
        ztmin, ztmax = self.check_axis(local_ray.origin[2],
                                       local_ray.direction[2])

        tmin = max(xtmin, ytmin, ztmin)
        tmax = min(xtmax, ytmax, ztmax)

        # ray misses cube?
        if tmin > tmax:
            return []

        return [Intersection(tmin, self), Intersection(tmax, self)]

    def check_axis(self, origin, direction):
        tmin_numerator = (-1 - origin)
        tmax_numerator = (1 - origin)

        if abs(direction) >= self.EPSILON:
            tmin = tmin_numerator / direction
            tmax = tmax_numerator / direction
        else:
            tmin = tmin_numerator * inf
            tmax = tmax_numerator * inf

        if tmin > tmax:
            tmin, tmax = tmax, tmin

        return (tmin, tmax)

    def local_normal_at(self, local_point):
        maxc = max(abs(local_point[0]), abs(local_point[1]),
                   abs(local_point[2]))

        if maxc == abs(local_point[0]):
            return vector(local_point[0], 0, 0)

        if maxc == abs(local_point[1]):
            return vector(0, local_point[1], 0)

        return vector(0, 0, local_point[2])
