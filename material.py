from tuples import color, hadamard, normalize, add, subtract, multiply, dot, negate, reflect


class Material:
    def __init__(self):
        self.color = color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0
        self.reflective = 0.0
        self.transparency = 0.0
        self.refractive_index = 1.0
        self.pattern = None

    @classmethod
    def from_yaml(cls, data):
        material = cls()

        material_data = data['material']
        if 'color' in material_data:
            values = material_data['color']
            material.color = color(values[0], values[1], values[2])

        if 'ambient' in material_data:
            material.ambient = material_data['ambient']

        if 'diffuse' in material_data:
            material.diffuse = material_data['diffuse']

        if 'specular' in material_data:
            material.specular = material_data['specular']

        if 'shininess' in material_data:
            material.shininess = material_data['shininess']

        if 'reflective' in material_data:
            material.reflective = material_data['reflective']

        return material

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False


def lighting(material, shape, light, point, eyev, normalv, in_shadow=False):
    if material.pattern is not None:
        effective_color = material.pattern.pattern_at_shape(shape, point)
    else:
        effective_color = hadamard(material.color, light.intensity)

    lightv = normalize(subtract(light.position, point))

    ambient = multiply(effective_color, material.ambient)

    light_dot_normal = dot(lightv, normalv)
    if light_dot_normal < 0:
        diffuse = color(0, 0, 0)
        specular = color(0, 0, 0)
    else:
        diffuse = multiply(effective_color,
                           material.diffuse * light_dot_normal)
        reflectv = reflect(negate(lightv), normalv)
        reflect_dot_eye = dot(reflectv, eyev)
        if reflect_dot_eye <= 0:
            specular = color(0, 0, 0)
        else:
            factor = reflect_dot_eye**material.shininess
            specular = multiply(light.intensity, material.specular * factor)

    if in_shadow:
        return ambient

    return add(ambient, add(diffuse, specular))
