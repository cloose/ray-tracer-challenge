from math import tan
from core import Ray, point, vector, normalize, subtract, identity_matrix, inverse, multiply_tuple, view_transform


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

    @classmethod
    def from_yaml(cls, data):
        camera = cls(data['width'], data['height'], data['field-of-view'])

        values = data['from']
        from_pos = point(values[0], values[1], values[2])

        values = data['to']
        to_pos = point(values[0], values[1], values[2])

        values = data['up']
        up_vector = vector(values[0], values[1], values[2])

        camera.set_transform(view_transform(from_pos, to_pos, up_vector))
        return camera

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
