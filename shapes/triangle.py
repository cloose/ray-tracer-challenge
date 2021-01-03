from core import Intersection, add, subtract, multiply, cross, dot, normalize
from .shape import Shape


class Triangle(Shape):
    def __init__(self, p1, p2, p3, n1=None, n2=None, n3=None):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

        self.smoothed = False

        # pre-compute edge vectors
        self.e1 = subtract(p2, p1)
        self.e2 = subtract(p3, p1)

        # pre-compute normal
        self.normal = normalize(cross(self.e2, self.e1))

    @classmethod
    def smooth_triangle(cls, p1, p2, p3, n1, n2, n3):
        triangle = cls(p1, p2, p3, n1, n2, n3)
        triangle.smoothed = True
        return triangle

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

        if self.smoothed:
            return [Intersection(t, self, u, v)]

        return [Intersection(t, self)]

    def local_normal_at(self, local_point, hit=None):
        if self.smoothed:
            return add(
                multiply(self.n2, hit.u),
                add(multiply(self.n3, hit.v),
                    multiply(self.n1, (1 - hit.u - hit.v))))

        return self.normal
