from math import inf, sqrt
from core import Intersection, vector, transform_from_yaml, normalize
from .material import Material
from .shape import Shape


class Cylinder(Shape):
    EPSILON = 0.00001

    def __init__(self):
        super().__init__()

        self.minimum = -inf
        self.maximum = inf
        self.closed = False

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
            xs = []
            self.intersect_caps(local_ray, xs)
            return xs

        b = 2 * local_ray.origin[0] * local_ray.direction[0] + \
            2 * local_ray.origin[2] * local_ray.direction[2]
        c = local_ray.origin[0]**2 + local_ray.origin[2]**2 - 1

        discriminant = b**2 - 4 * a * c

        # ray does not intersect the cylinder
        if discriminant < 0:
            return []

        t0 = (-b - sqrt(discriminant)) / (2 * a)
        t1 = (-b + sqrt(discriminant)) / (2 * a)

        if t0 > t1:
            t0, t1 = t1, t0

        xs = []

        y0 = local_ray.origin[1] + t0 * local_ray.direction[1]
        if self.minimum < y0 < self.maximum:
            xs.append(Intersection(t0, self))

        y1 = local_ray.origin[1] + t1 * local_ray.direction[1]
        if self.minimum < y1 < self.maximum:
            xs.append(Intersection(t1, self))

        self.intersect_caps(local_ray, xs)

        return xs

    def intersect_caps(self, ray, xs):
        # caps only matter if the cylinder is closed, and might possibly be
        # intersected by the ray.
        if not self.closed or abs(ray.direction[1]) < self.EPSILON:
            return []

        # check for an intersection with the lower end cap by intersecting
        # the ray with the plane at y=cyl.minimum
        t = (self.minimum - ray.origin[1]) / ray.direction[1]
        if self.check_cap(ray, t):
            xs.append(Intersection(t, self))

        # check for an intersection with the upper end cap by intersecting
        # the ray with the plane at y=cyl.maximum
        t = (self.maximum - ray.origin[1]) / ray.direction[1]
        if self.check_cap(ray, t):
            xs.append(Intersection(t, self))

    # checks to see if the intersection at `t` is within a radius
    # of 1 (the radius of your cylinders) from the y axis.
    def check_cap(self, ray, t):
        x = ray.origin[0] + t * ray.direction[0]
        z = ray.origin[2] + t * ray.direction[2]
        return (x**2 + z**2) <= 1

    def local_normal_at(self, local_point):
        # compute the square of the distance from the y axis
        dist = local_point[0]**2 + local_point[2]**2

        if dist < 1 and local_point[1] >= self.maximum - self.EPSILON:
            return vector(0, 1, 0)

        if dist < 1 and local_point[1] <= self.minimum + self.EPSILON:
            return vector(0, -1, 0)

        return vector(local_point[0], 0, local_point[2])
