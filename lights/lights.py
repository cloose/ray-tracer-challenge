from core import color, point


class PointLight:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity
        self.samples = 1

    @classmethod
    def from_yaml(cls, data):
        values = data['at']
        position = point(values[0], values[1], values[2])

        values = data['intensity']
        intensity = color(values[0], values[1], values[2])

        return cls(position, intensity)

    def intensity_at(self, p, world):
        if world.is_shadowed(self.position, p):
            return 0.0

        return 1.0

    def get_samples(self):
        yield self.position
