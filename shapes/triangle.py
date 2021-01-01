from core import Intersection, subtract, cross, dot, normalize
from .shape import Shape


class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        # pre-compute edge vectors
        self.e1 = subtract(p2, p1)
        self.e2 = subtract(p3, p1)

        # pre-compute normal
        self.normal = normalize(cross(self.e2, self.e1))

    def local_intersect(self, local_ray):
        dir_cross_e2 = cross(local_ray.direction, self.e2)
        determinant = dot(self.e1, dir_cross_e2)
        if abs(determinant) < self.EPSILON:
            return []

        f = 1.0 / determinant
        p1_to_origin = subtract(local_ray.origin, self.p1)
        u = f * dot(p1_to_origin, dir_cross_e2)
        if u < 0.0 or u > 1.0:
            return []

        origin_cross_e1 = cross(p1_to_origin, self.e1)
        v = f * dot(local_ray.direction, origin_cross_e1)
        if v < 0.0 or (u + v) > 1.0:
            return []

        t = f * dot(self.e2, origin_cross_e1)
        return [Intersection(t, self)]

    def local_normal_at(self, local_point):
        return self.normal
