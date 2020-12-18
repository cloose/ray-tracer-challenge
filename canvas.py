from tuples import color


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [color(0, 0, 0)] * (width * height)

    def set_pixel(self, x, y, color):
        self.pixels[x + y * self.width] = color

    def pixel_at(self, x, y):
        return self.pixels[x + y * self.width]

    def to_ppm(self):
        return \
"""P3
{width} {height}
255
{pixels}
""".format(width=self.width, height=self.height, pixels=self.pixels_to_string())

    def pixels_to_string(self):
        data = []
        for y in range(self.height):
            line = ''
            for x in range(self.width):
                px = self.pixel_at(x, y)
                for c in range(3):
                    color = f'{clamp(px[c])}'
                    if len(line) + len(color) < 70:
                        line += color + ' '
                    else:
                        data.append(line.strip() + '\n')
                        line = color + ' '
            data.append(line.strip() + '\n')
        return ''.join(data)


def clamp(c):
    scaled = round(c * 255)
    return min(max(scaled, 0), 255)
