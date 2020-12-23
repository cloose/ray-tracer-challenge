from core import color, point


class PointLight:
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

    @classmethod
    def from_yaml(cls, data):
        values = data['at']
        position = point(values[0], values[1], values[2])

        values = data['intensity']
        intensity = color(values[0], values[1], values[2])

        return cls(position, intensity)
