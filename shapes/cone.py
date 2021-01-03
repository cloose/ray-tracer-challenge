from math import inf, sqrt
from core import Intersection, vector, transform_from_yaml
from .shape import Shape, Material


class Cone(Shape):
    def __init__(self):
        super().__init__()

        self.minimum = -inf
        self.maximum = inf
        self.closed = False

    @classmethod
    def from_yaml(cls, data):
        cone = cls()

        if 'min' in data:
            cone.minimum = data['min']

        if 'max' in data:
            cone.maximum = data['max']

        if 'closed' in data:
            cone.closed = data['closed']

        if 'transform' in data:
            cone.set_transform(transform_from_yaml(data))

        if 'material' in data:
            cone.material = Material.from_yaml(data)

        return cone

    def local_intersect(self, local_ray):
        a = local_ray.direction[0]**2 - \
            local_ray.direction[1]**2 + \
            local_ray.direction[2]**2
        b = 2 * local_ray.origin[0] * local_ray.direction[0] - \
            2 * local_ray.origin[1] * local_ray.direction[1] + \
            2 * local_ray.origin[2] * local_ray.direction[2]

        if abs(a) < self.EPSILON and abs(b) < self.EPSILON:
            return []

        c = local_ray.origin[0]**2 - \
            local_ray.origin[1]**2 + \
            local_ray.origin[2]**2

        if abs(a) < self.EPSILON:
            t = -c / (2 * b)
            xs = [Intersection(t, self)]
            self.intersect_caps(local_ray, xs)
            return xs

        discriminant = b**2 - 4 * a * c

        # ray does not intersect the cone
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
        if self.check_cap(ray, t, self.minimum):
            xs.append(Intersection(t, self))

        # check for an intersection with the upper end cap by intersecting
        # the ray with the plane at y=cyl.maximum
        t = (self.maximum - ray.origin[1]) / ray.direction[1]
        if self.check_cap(ray, t, self.maximum):
            xs.append(Intersection(t, self))

    # checks to see if the intersection at `t` is within a radius
    # of 1 (the radius of your cylinders) from the y axis.
    def check_cap(self, ray, t, radius):
        x = ray.origin[0] + t * ray.direction[0]
        z = ray.origin[2] + t * ray.direction[2]
        return (x**2 + z**2) <= radius**2

    def local_normal_at(self, local_point, hit=None):
        # compute the square of the distance from the y axis
        dist = local_point[0]**2 + local_point[2]**2

        if dist < 1 and local_point[1] >= self.maximum - self.EPSILON:
            return vector(0, 1, 0)

        if dist < 1 and local_point[1] <= self.minimum + self.EPSILON:
            return vector(0, -1, 0)

        y = sqrt(local_point[0]**2 + local_point[2]**2)
        if local_point[1] > 0:
            y = -y

        return vector(local_point[0], y, local_point[2])
