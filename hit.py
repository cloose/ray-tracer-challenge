from math import sqrt
from tuples import negate, dot, add, subtract, multiply, reflect


class Hit:
    EPSILON = 0.00001

    def __init__(self, intersection, ray, intersections=None):
        if intersections is None:
            intersections = [intersection]

        self.t = intersection.t
        self.object = intersection.object

        self.point = ray.position_at(self.t)
        self.eyev = negate(ray.direction)
        self.normalv = self.object.normal_at(self.point)

        self.inside = dot(self.normalv, self.eyev) < 0
        if self.inside:
            self.normalv = negate(self.normalv)

        self.over_point = add(self.point, multiply(self.normalv, self.EPSILON))
        self.under_point = subtract(self.point,
                                    multiply(self.normalv, self.EPSILON))

        self.reflectv = reflect(ray.direction, self.normalv)

        containers = []

        for i in intersections:
            if i == intersection:
                if not containers:
                    self.n1 = 1.0
                else:
                    self.n1 = containers[-1].material.refractive_index

            if i.object in containers:
                containers.remove(i.object)
            else:
                containers.append(i.object)

            if i == intersection:
                if not containers:
                    self.n2 = 1.0
                else:
                    self.n2 = containers[-1].material.refractive_index
                break

    def schlick(self):
        """"""
        # find the cosine of the angle between the eye and normal vectors
        cos = dot(self.eyev, self.normalv)

        # total internal reflection can only occur if n1 > n2
        if self.n1 > self.n2:
            n_ratio = self.n1 / self.n2
            sin2_t = n_ratio**2 * (1.0 - cos**2)
            if sin2_t > 1.0:
                return 1.0

            # compute cosine of theta_t
            cos_t = sqrt(1.0 - sin2_t)

            # when n1>n2 use cosine of theta_t instead
            cos = cos_t

        r0 = ((self.n1 - self.n2) / (self.n1 + self.n2))**2
        return r0 + (1.0 - r0) * (1 - cos)**5
