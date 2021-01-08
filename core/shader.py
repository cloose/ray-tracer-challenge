from .tuples import color, hadamard, normalize, add, subtract, multiply, dot, negate, reflect


def lighting(material, shape, light, point, eyev, normalv, in_shadow=False):
    if material.pattern is not None:
        effective_color = material.pattern.pattern_at_shape(shape, point)
    else:
        effective_color = hadamard(material.color, light.intensity)

    # find the direction to the light source
    lightv = normalize(subtract(light.position, point))

    # compute the ambient contribution
    ambient = multiply(effective_color, material.ambient)

    # light_dot_normal represents the cosine of the angle between the
    # light vector and the normal vector. A negative number means the
    # light is on the other side of the surface.
    light_dot_normal = dot(lightv, normalv)
    if light_dot_normal < 0:
        diffuse = color(0, 0, 0)
        specular = color(0, 0, 0)
    else:
        # compute the diffuse contribution
        diffuse = multiply(effective_color,
                           material.diffuse * light_dot_normal)

        reflectv = reflect(negate(lightv), normalv)

        # reflect_dot_eye represents the cosine of the angle between the
        # reflection vector and the eye vector. A negative number means the
        # light reflects away from the eye.
        reflect_dot_eye = dot(reflectv, eyev)
        if reflect_dot_eye <= 0:
            specular = color(0, 0, 0)
        else:
            # compute the specular contribution
            factor = reflect_dot_eye**material.shininess
            specular = multiply(light.intensity, material.specular * factor)

    if in_shadow:
        return ambient

    return add(ambient, add(diffuse, specular))
