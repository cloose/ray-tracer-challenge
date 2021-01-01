from core import color


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

        if 'transparency' in material_data:
            material.transparency = material_data['transparency']

        if 'refractive-index' in material_data:
            material.refractive_index = material_data['refractive-index']

        return material

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False
