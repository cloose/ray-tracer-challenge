from .tuples import (add, color, dot, hadamard, multiply, negate, normalize,
                     reflect, subtract)


def lighting(material, shape, light, point, eyev, normalv, light_intensity):
    if material.pattern is not None:
        effective_color = material.pattern.pattern_at_shape(shape, point)
    else:
        effective_color = hadamard(material.color, light.intensity)

    # compute the ambient contribution
    ambient = multiply(effective_color, material.ambient)

    sum = color(0, 0, 0)
    for light_position in light.get_samples():
        # find the direction to the light source
        lightv = normalize(subtract(light_position, point))

        # light_dot_normal represents the cosine of the angle between the
        # light vector and the normal vector. A negative number means the
        # light is on the other side of the surface.
        light_dot_normal = dot(lightv, normalv)
        if light_dot_normal < 0:
            continue

        # compute the diffuse contribution
        diffuse = multiply(effective_color,
                           material.diffuse * light_dot_normal)
        sum = add(sum, diffuse)

        reflectv = reflect(negate(lightv), normalv)

        # reflect_dot_eye represents the cosine of the angle between the
        # reflection vector and the eye vector. A negative number means the
        # light reflects away from the eye.
        reflect_dot_eye = dot(reflectv, eyev)
        if reflect_dot_eye > 0:
            # compute the specular contribution
            factor = reflect_dot_eye**material.shininess
            specular = multiply(light.intensity, material.specular * factor)
            sum = add(sum, specular)

    return add(ambient, \
               multiply(multiply(sum, 1/light.samples), light_intensity))
