from .shape import Shape


class Group(Shape):
    def __init__(self):
        super().__init__()

        self.children = []

    def add_child(self, shape):
        self.children.append(shape)
        shape.parent = self

    def local_intersect(self, local_ray):
        return sorted([
            xs for child in self.children for xs in child.intersect(local_ray)
        ])

    def local_normal_at(self, local_point):
        raise NotImplementedError('groups do not support local_normal_at')
