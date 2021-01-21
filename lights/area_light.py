from core import (DeterministicSequence, RandomSequence, add, color, multiply,
                  point, vector)


class AreaLight:
    def __init__(self, corner, full_uvec, usteps, full_vvec, vsteps,
                 intensity):
        self.corner = corner
        self.uvec = multiply(full_uvec, 1 / usteps)
        self.usteps = usteps
        self.vvec = multiply(full_vvec, 1 / vsteps)
        self.vsteps = vsteps
        self.samples = usteps * vsteps
        self.position = add(add(corner, multiply(full_uvec, 1 / 2)),
                            multiply(full_vvec, 1 / 2))
        self.intensity = intensity
        self.jitter_by = DeterministicSequence([0.5])

    @classmethod
    def from_yaml(cls, data):
        values = data['corner']
        corner = point(values[0], values[1], values[2])

        values = data['uvec']
        uvec = vector(values[0], values[1], values[2])
        usteps = data['usteps']

        values = data['vvec']
        vvec = vector(values[0], values[1], values[2])
        vsteps = data['vsteps']

        values = data['intensity']
        intensity = color(values[0], values[1], values[2])

        light = cls(corner, uvec, usteps, vvec, vsteps, intensity)

        if 'jitter' in data and data['jitter']:
            light.jitter_by = RandomSequence()

        return light

    def point_on_light(self, u, v):
        return add(self.corner, \
               add(multiply(self.uvec, (u + self.jitter_by.next())), \
                   multiply(self.vvec, (v + self.jitter_by.next()))))

    def intensity_at(self, p, world):
        total = 0.0

        # for light_position in self.get_samples():
        for v in range(0, self.vsteps):
            for u in range(0, self.usteps):
                light_position = self.point_on_light(u, v)
                if not world.is_shadowed(light_position, p):
                    total += 1.0

        return total / self.samples

    def get_samples(self):
        for v in range(0, self.vsteps):
            for u in range(0, self.usteps):
                yield self.point_on_light(u, v)
