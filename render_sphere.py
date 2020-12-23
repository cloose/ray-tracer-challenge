# pylint: disable=invalid-name

from core import point, color, normalize, subtract, scaling
from canvas import Canvas
from shapes import Sphere
from rays import Ray
from intersection import hit


def main():
    canvas = Canvas(100, 100)
    red = color(1, 0, 0)
    shape = Sphere()

    # shrink it along the y axis
    shape.transform = scaling(1, 0.5, 1)

    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 7.0

    pixel_size = wall_size / 100
    half = wall_size / 2

    for y in range(100):
        world_y = half - pixel_size * y

        for x in range(100):
            world_x = -half + pixel_size * x

            pos = point(world_x, world_y, wall_z)

            r = Ray(ray_origin, normalize(subtract(pos, ray_origin)))
            xs = shape.intersect(r)

            if hit(xs) is not None:
                canvas.set_pixel(x, y, red)

    ppm = canvas.to_ppm()
    f = open('render_sphere.ppm', 'w')
    f.write(ppm)


if __name__ == "__main__":
    main()
