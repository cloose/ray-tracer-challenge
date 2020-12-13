from canvas import Canvas


class RayTracer():
    def __init__(self):
        pass

    def render(self, camera, world):
        """render world into canvas"""

        image = Canvas(camera.horizontal_size_px, camera.vertical_size_px)

        for y in range(camera.vertical_size_px):
            for x in range(camera.horizontal_size_px):
                ray = camera.ray_for_pixel(x, y)
                color = world.color_at(ray)
                image.set_pixel(x, y, color)

        return image
