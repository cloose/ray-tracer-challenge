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
