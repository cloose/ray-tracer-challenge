from tuples import point, vector, add, normalize


def tick(env, proj):
    position = add(proj['position'], proj['velocity'])
    velocity = add(add(proj['velocity'], env['gravity']), env['wind'])
    return dict(position=position, velocity=velocity)


def main():
    p = dict(position=point(0, 1, 0), velocity=normalize(vector(1, 1, 0)))
    e = dict(gravity=vector(0, -0.1, 0), wind=vector(-0.01, 0, 0))

    while p['position'][1] > 0.0:
        print('position %r, %r, %r' %
              (p['position'][0], p['position'][1], p['position'][2]))
        p = tick(e, p)


if __name__ == "__main__":
    main()
