from math import pi

from core import (Canvas, color, multiply_matrix, multiply_tuple, point,
                  rotation_y, scaling, translation)


def main():
    c = Canvas(500, 500)

    p = point(0, 0, 1)

    translate = translation(250, 0, 250)
    scale = scaling(100, 0, 100)

    for h in range(12):
        r = rotation_y(h * pi / 6)
        transform = multiply_matrix(translate, multiply_matrix(scale, r))
        p2 = multiply_tuple(transform, p)
        print(f"position ({p2[0]}, {p2[1]}, {p2[2]})")
        c.set_pixel(round(p2[0]), c.height - round(p2[2]),
                    color(0.0, 1.0, 0.0))

    with open('clock.ppm', 'w') as out_file:
        out_file.write(c.to_ppm())


if __name__ == "__main__":
    main()
