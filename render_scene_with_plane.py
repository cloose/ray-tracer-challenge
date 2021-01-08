from math import pi
from core import point, vector, color, multiply_matrix
from core import scaling, translation, rotation_y, view_transform
from shapes import Material, Sphere, Plane
from lights import PointLight
from scene import Camera, World, RayTracer
from patterns import StripePattern


def render_scene_with_plane():
    floor = Plane()
    floor.set_transform(scaling(10, 0.01, 10))
    # floor.set_transform(
    # multiply_matrix(translation(0, 0.33, 0), scaling(10, 0.01, 10)))
    floor.material = Material()
    floor.material.color = color(1, 0.9, 0.9)
    floor.material.specular = 0

    # left_wall = Plane()
    # left_wall.set_transform(
    #     multiply_matrix(
    #         translation(0, 0, 5),
    #         multiply_matrix(rotation_y(-pi / 4),
    #                  multiply_matrix(rotation_x(pi / 2), scaling(10, 0.01, 10)))))
    # left_wall.material = floor.material

    # right_wall = Plane()
    # right_wall.set_transform(
    #     multiply_matrix(
    #         translation(0, 0, 5),
    #         multiply_matrix(rotation_y(pi / 4),
    #                  multiply_matrix(rotation_x(pi / 2), scaling(10, 0.01, 10)))))

    middle = Sphere()
    middle.set_transform(translation(-0.5, 1, 0.5))
    middle.material = Material()
    middle.material.pattern = StripePattern(color(0.6, 1.0, 0.6),
                                            color(0.3, 0.6, 0.3))
    middle.material.color = color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3

    middle.material.pattern.set_transform(
        multiply_matrix(scaling(0.2, 0.2, 0.2), rotation_y(pi / 4)))

    right = Sphere()
    right.set_transform(
        multiply_matrix(translation(1.5, 0.5, -0.5), scaling(0.5, 0.5, 0.5)))
    right.material = Material()
    right.material.color = color(0.5, 1, 0.1)
    # right.material.diffuse = 0.7
    right.material.diffuse = 0.2
    right.material.specular = 0.3
    right.material.reflective = 0.7

    left = Sphere()
    left.set_transform(
        multiply_matrix(translation(-1.5, 0.33, -0.75),
                        scaling(0.33, 0.33, 0.33)))
    left.material = Material()
    left.material.color = color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3

    world = World()
    world.add_light(PointLight(point(-10, 10, -10), color(1, 1, 1)))
    world.objects.append(floor)
    # world.objects.append(left_wall)
    # world.objects.append(right_wall)
    world.objects.append(middle)
    world.objects.append(right)
    world.objects.append(left)

    camera = Camera(600, 500, pi / 3)
    camera.set_transform(
        view_transform(point(0, 1.5, -5), point(0, 1, 0), vector(0, 1, 0)))
    # camera.set_transform(
    # view_transform(point(0, 4, -1), point(0, 1, 0), vector(0, 1, 0)))

    canvas = RayTracer().render(camera, world)
    ppm = canvas.to_ppm()
    outf = open('render_scene_with_plane.ppm', 'w')
    outf.write(ppm)


if __name__ == "__main__":
    render_scene_with_plane()
