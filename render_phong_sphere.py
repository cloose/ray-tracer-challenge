from core import point, color, normalize, subtract, negate, scaling
from canvas import Canvas
from shapes import Sphere
from rays import Ray
from intersection import hit
from material import Material
from shader import lighting
from lights import PointLight


def main():
    canvas_pixels = 500
    canvas = Canvas(canvas_pixels, canvas_pixels)
    shape = Sphere()

    # shrink it along the y axis
    shape.transform = scaling(1, 0.5, 1)

    # assign material
    shape.material = Material()
    shape.material.color = color(1, 0.2, 1)

    light_position = point(-10, 10, -10)
    light_color = color(1, 1, 1)
    light = PointLight(light_position, light_color)

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

            shape_hit = hit(xs)
            if shape_hit is not None:
                hit_point = r.position_at(shape_hit.t)
                normal = shape_hit.object.normal_at(hit_point)
                eye = negate(r.direction)
                px_color = lighting(shape_hit.object.material,
                                    shape_hit.object, light, hit_point, eye,
                                    normal)
                canvas.set_pixel(x, y, px_color)

    ppm = canvas.to_ppm()
    f = open('render_phong_sphere.ppm', 'w')
    f.write(ppm)


if __name__ == "__main__":
    main()
