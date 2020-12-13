from tuples import point, color, subtract, magnitude, normalize
from transformations import scaling
from lights import PointLight
from sphere import Sphere
from material import Material, lighting
from rays import Ray
from intersection import hit as hit_at
from hit import Hit


class World:
    def __init__(self):
        self.light = None
        self.objects = []

    @classmethod
    def default(cls):
        world = cls()
        world.light = PointLight(point(-10, 10, -10), color(1, 1, 1))

        sphere1 = Sphere()
        mat = Material()
        mat.color = color(0.8, 1.0, 0.6)
        mat.diffuse = 0.7
        mat.specular = 0.2
        sphere1.material = mat

        sphere2 = Sphere()
        sphere2.set_transform(scaling(0.5, 0.5, 0.5))

        world.objects.append(sphere1)
        world.objects.append(sphere2)

        return world

    def intersect(self, ray):
        return sorted(
            [xs for obj in self.objects for xs in obj.intersect(ray)])

    def shade_hit(self, hit):
        shadowed = self.is_shadowed(hit.over_point)
        return lighting(hit.object.material, hit.object, self.light, hit.point,
                        hit.eyev, hit.normalv, shadowed)

    def color_at(self, ray):
        intersections = self.intersect(ray)
        hit_intersection = hit_at(intersections)
        if hit_intersection is None:
            return color(0, 0, 0)

        shape_hit = Hit(hit_intersection, ray)
        return self.shade_hit(shape_hit)

    def is_shadowed(self, point):
        vec = subtract(self.light.position, point)
        distance = magnitude(vec)
        direction = normalize(vec)

        ray = Ray(point, direction)
        intersections = self.intersect(ray)
        hit_intersection = hit_at(intersections)
        return hit_intersection is not None and hit_intersection.t < distance
