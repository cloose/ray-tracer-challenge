from math import sqrt
from core import Intersection, vector, transform_from_yaml, normalize
from .material import Material
from .shape import Shape


class Cylinder(Shape):
    EPSILON = 0.00001

    def __init__(self):
        super().__init__()

    @classmethod
    def from_yaml(cls, data):
        cylinder = cls()

        if 'transform' in data:
            cylinder.set_transform(transform_from_yaml(data))

        if 'material' in data:
            cylinder.material = Material.from_yaml(data)

        return cylinder

    def local_intersect(self, local_ray):
        a = local_ray.direction[0]**2 + local_ray.direction[2]**2

        # ray is parallel to the y axis?
        if abs(a) < self.EPSILON:
            return []

        b = 2 * local_ray.origin[0] * local_ray.direction[0] + \
            2 * local_ray.origin[2] * local_ray.direction[2]
        c = local_ray.origin[0]**2 + local_ray.origin[2]**2 - 1

        discriminant = b**2 - 4 * a * c

        # ray does not intersect the cylinder
        if discriminant < 0:
            return []

        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)

        return [Intersection(t1, self), Intersection(t2, self)]

    def local_normal_at(self, local_point):
        return vector(local_point[0], 0, local_point[2])
