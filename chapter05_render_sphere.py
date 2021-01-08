from math import pi

from core import (Canvas, Ray, color, hit, multiply_matrix, normalize, point,
                  rotation_z, scaling, shearing, subtract)
from shapes import Sphere


def main():
    canvas_pixels = 400
    canvas = Canvas(canvas_pixels, canvas_pixels)
    red = color(1, 0, 0)
    shape = Sphere()

    # shrink it along the y axis
    #shape.set_transform(scaling(1, 0.5, 1))
    # shrink it along the x axis
    #shape.set_transform(scaling(0.5, 1, 1))
    # shrink it, and rotate it!
    # shape.set_transform(multiply_matrix(rotation_z(pi / 4), scaling(0.5, 1,
    #                                                                 1)))
    # shrink it, and skew it!
    # shape.set_transform(
    #     multiply_matrix(shearing(1, 0, 0, 0, 0, 0), scaling(0.5, 1, 1)))

    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 7.0

    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    for y in range(canvas_pixels):
        world_y = half - pixel_size * y

        for x in range(canvas_pixels):
            world_x = -half + pixel_size * x

            pos = point(world_x, world_y, wall_z)

            r = Ray(ray_origin, normalize(subtract(pos, ray_origin)))
            xs = shape.intersect(r)

            if hit(xs) is not None:
                canvas.set_pixel(x, y, red)

    with open('render_sphere.ppm', 'w') as out_file:
        out_file.write(canvas.to_ppm())


if __name__ == "__main__":
    main()
