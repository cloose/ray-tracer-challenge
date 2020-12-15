from tuples import negate, dot, add, multiply, reflect


class Hit:
    EPSILON = 0.00001

    def __init__(self, intersection, ray):
        self.t = intersection.t
        self.object = intersection.object

        self.point = ray.position_at(self.t)
        self.eyev = negate(ray.direction)
        self.normalv = self.object.normal_at(self.point)

        self.inside = dot(self.normalv, self.eyev) < 0
        if self.inside:
            self.normalv = negate(self.normalv)

        self.over_point = add(self.point, multiply(self.normalv, self.EPSILON))

        self.reflectv = reflect(ray.direction, self.normalv)
