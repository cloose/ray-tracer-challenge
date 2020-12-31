from core import normalize, identity_matrix, inverse, multiply_tuple, transpose
from .material import Material


class Shape:
    EPSILON = 1e-9

    def __init__(self):
        self.__transform = identity_matrix()
        self.__inverse_transform = identity_matrix()
        self.material = Material()
        self.parent = None

    def set_transform(self, transformation_matrix):
        """set transformation matrix for the shape"""
        self.__transform = transformation_matrix
        self.__inverse_transform = inverse(transformation_matrix)

    def transform(self):
        return self.__transform

    def inverse_transform(self):
        return self.__inverse_transform

    def world_to_object(self, point):
        if self.parent:
            point = self.parent.world_to_object(point)

        return multiply_tuple(self.__inverse_transform, point)

    def normal_to_world(self, normal):
        normal = multiply_tuple(transpose(self.__inverse_transform), normal)
        normal[3] = 0
        normal = normalize(normal)

        if self.parent:
            normal = self.parent.normal_to_world(normal)

        return normal

    def intersect(self, ray):
        local_ray = ray.transformed(self.__inverse_transform)
        return self.local_intersect(local_ray)

    def local_intersect(self, local_ray):
        raise NotImplementedError('subclass must override local_intersect')

    def normal_at(self, world_point):
        local_point = self.world_to_object(world_point)
        local_normal = self.local_normal_at(local_point)
        return self.normal_to_world(local_normal)

    def local_normal_at(self, local_point):
        raise NotImplementedError('subclass must override local_normal_at')
