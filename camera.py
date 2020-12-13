from math import tan
from tuples import point, normalize, subtract
from matrix import identity_matrix, inverse, multiply_tuple
from rays import Ray


class Camera:
    def __init__(self, hsize, vsize, fov):
        self.horizontal_size_px = hsize
        self.vertical_size_px = vsize
        self.field_of_view = fov
        self.__transform = identity_matrix()
        self.__inverse_transform = identity_matrix()

        half_view = tan(self.field_of_view / 2)
        aspect = self.horizontal_size_px / self.vertical_size_px

        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view

        self.pixel_size = (self.half_width * 2) / self.horizontal_size_px

    def set_transform(self, transformation_matrix):
        self.__transform = transformation_matrix
        self.__inverse_transform = inverse(transformation_matrix)

    def transform(self):
        return self.__transform

    def inverse_transform(self):
        return self.__inverse_transform

    def ray_for_pixel(self, pixel_x, pixel_y):
        xoffset = (pixel_x + 0.5) * self.pixel_size
        yoffset = (pixel_y + 0.5) * self.pixel_size

        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset

        pixel = multiply_tuple(self.__inverse_transform,
                               point(world_x, world_y, -1))
        origin = multiply_tuple(self.__inverse_transform, point(0, 0, 0))
        direction = normalize(subtract(pixel, origin))

        return Ray(origin, direction)
