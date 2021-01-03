from .shape import Shape


class CsgShape(Shape):
    def __init__(self, operation, left, right):
        super().__init__()

        self.operation = operation
        self.left = left
        self.right = right

        self.left.parent = self
        self.right.parent = self

    def local_intersect(self, local_ray):
        left_xs = self.left.intersect(local_ray)
        right_xs = self.right.intersect(local_ray)

        xs = sorted(left_xs + right_xs)

        return self.filter_intersections(xs)

    def local_normal_at(self, local_point, hit=None):
        raise NotImplementedError('csg shape does not support local_normal_at')

    def filter_intersections(self, intersections):
        # begin outside of both children
        inside_left = False
        inside_right = False

        result = []

        for i in intersections:
            # if i.object is part of the "left" child, then left_hit is true
            left_hit = self.left.includes(i.object)

            if intersection_allowed(self.operation, left_hit, inside_left,
                                    inside_right):
                result.append(i)

            if left_hit:
                inside_left = not inside_left
            else:
                inside_right = not inside_right

        return result

    def includes(self, other):
        return self.left.includes(other) or self.right.includes(other)


def intersection_allowed(op, left_hit, inside_left, inside_right):
    if op == "union":
        return (left_hit and not inside_right) or \
               (not left_hit and not inside_left)

    if op == "intersection":
        return (left_hit and inside_right) or \
               (not left_hit and inside_left)

    if op == "difference":
        return (left_hit and not inside_right) or \
               (not left_hit and inside_left)

    return False
