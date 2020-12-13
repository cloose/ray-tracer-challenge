from math import pi
from tuples import point, color
from matrix import multiply, multiply_tuple
from transformations import translation, scaling, rotation_y
from canvas import Canvas


def main():
    c = Canvas(500, 500)

    p = point(0, 0, 1)

    translate = translation(250, 0, 250)
    scale = scaling(100, 0, 100)

    for h in range(12):
        r = rotation_y(h * pi / 6)
        transform = multiply(translate, multiply(scale, r))
    p2 = multiply_tuple(transform, p)
    print('position %r, %r, %r' % (p2[0], p2[1], p2[2]))
    c.set_pixel(round(p2[0]), c.height - round(p2[2]), color(0.0, 1.0, 0.0))

    ppm = c.to_ppm()
    f = open('clock.ppm', 'w')
    f.write(ppm)


if __name__ == "__main__":
    main()
