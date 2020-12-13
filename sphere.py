from math import sqrt
from tuples import point, subtract, dot
from intersection import Intersection
from shape import Shape


class Sphere(Shape):
    def __init__(self):
        Shape.__init__(self)

    def local_intersect(self, local_ray):
        sphere_to_ray = subtract(local_ray.origin, point(0, 0, 0))

        a = dot(local_ray.direction, local_ray.direction)
        b = 2 * dot(local_ray.direction, sphere_to_ray)
        c = dot(sphere_to_ray, sphere_to_ray) - 1

        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            return []

        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)

        i1 = Intersection(t1, self)
        i2 = Intersection(t2, self)
        return [i1, i2]

    def local_normal_at(self, local_point):
        return subtract(local_point, point(0, 0, 0))
