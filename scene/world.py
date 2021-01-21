from math import sqrt

from core import Hit, Ray, add, color, dot
from core import hit as hit_at
from core import (lighting, magnitude, multiply, normalize, point, scaling,
                  subtract)
from lights import PointLight
from shapes import Material, Sphere


class World:
    def __init__(self):
        self.lights = []
        self.objects = []

    @classmethod
    def default(cls):
        world = cls()
        world.add_light(PointLight(point(-10, 10, -10), color(1, 1, 1)))

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

    def add_light(self, light):
        self.lights.append(light)

    def intersect(self, ray):
        return sorted(
            [xs for obj in self.objects for xs in obj.intersect(ray)])

    def shade_hit(self, hit, remaining=5):
        surface = color(0, 0, 0)

        for light in self.lights:
            light_intensity = light.intensity_at(hit.over_point, self)
            surface = add(
                surface,
                lighting(hit.object.material, hit.object, light, hit.point,
                         hit.eyev, hit.normalv, light_intensity))

        reflected = self.reflected_color(hit, remaining)
        refracted = self.refracted_color(hit, remaining)

        material = hit.object.material
        if material.reflective > 0 and material.transparency > 0:
            reflectance = hit.schlick()
            return add(add(surface, multiply(reflected, reflectance)),
                       multiply(refracted, (1 - reflectance)))
        return add(add(surface, reflected), refracted)

    def color_at(self, ray, remaining=5):
        intersections = self.intersect(ray)
        hit_intersection = hit_at(intersections)
        if hit_intersection is None:
            return color(0, 0, 0)

        shape_hit = Hit(hit_intersection, ray, intersections)
        return self.shade_hit(shape_hit, remaining)

    def reflected_color(self, hit, remaining=5):
        if remaining <= 0:
            return color(0, 0, 0)

        if hit.object.material.reflective == 0.0:
            return color(0, 0, 0)

        reflect_ray = Ray(hit.over_point, hit.reflectv)
        reflect_color = self.color_at(reflect_ray, remaining - 1)
        return multiply(reflect_color, hit.object.material.reflective)

    def refracted_color(self, hit, remaining=5):
        if remaining <= 0:
            return color(0, 0, 0)

        if hit.object.material.transparency == 0.0:
            return color(0, 0, 0)

        n_ratio = hit.n1 / hit.n2
        cos_i = dot(hit.eyev, hit.normalv)
        sin2_t = n_ratio**2 * (1 - cos_i**2)

        if sin2_t > 1.0:
            return color(0, 0, 0)

        cos_t = sqrt(1.0 - sin2_t)

        direction = subtract(multiply(hit.normalv, (n_ratio * cos_i - cos_t)),
                             multiply(hit.eyev, n_ratio))

        refract_ray = Ray(hit.under_point, direction)

        return multiply(self.color_at(refract_ray, remaining - 1),
                        hit.object.material.transparency)

    def is_shadowed(self, light_position, hit_point):
        vec = subtract(light_position, hit_point)
        distance = magnitude(vec)
        direction = normalize(vec)

        ray = Ray(hit_point, direction)
        intersections = self.intersect(ray)
        hit_intersection = hit_at(intersections)
        return hit_intersection is not None and hit_intersection.t < distance
