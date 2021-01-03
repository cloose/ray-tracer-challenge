from core import Intersection, vector, transform_from_yaml
from .material import Material
from .shape import Shape


class Plane(Shape):
    EPSILON = 0.00001

    def __init__(self):
        super().__init__()

    @classmethod
    def from_yaml(cls, data):
        plane = cls()

        if 'transform' in data:
            plane.set_transform(transform_from_yaml(data))

        if 'material' in data:
            plane.material = Material.from_yaml(data)

        return plane

    def local_intersect(self, local_ray):
        if abs(local_ray.direction[1]) < self.EPSILON:
            return []

        t = -local_ray.origin[1] / local_ray.direction[1]
        return [Intersection(t, self)]

    def local_normal_at(self, local_point, hit=None):
        return vector(0, 1, 0)
