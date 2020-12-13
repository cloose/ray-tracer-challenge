from math import sqrt


def tuple(x, y, z, w):
    return [x, y, z, w]


def point(x, y, z):
    return tuple(x, y, z, 1.0)


def vector(x, y, z):
    return tuple(x, y, z, 0.0)


def color(r, g, b):
    return tuple(r, g, b, 0.0)


def ispoint(tuple):
    return tuple[3] > 0.0


def isvector(tuple):
    return tuple[3] < 1.0


def add(t1, t2):
    return tuple(t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2], t1[3] + t2[3])


def subtract(t1, t2):
    return tuple(t1[0] - t2[0], t1[1] - t2[1], t1[2] - t2[2], t1[3] - t2[3])


def negate(t):
    return tuple(-t[0], -t[1], -t[2], -t[3])


def multiply(t, scalar):
    return tuple(t[0] * scalar, t[1] * scalar, t[2] * scalar, t[3] * scalar)


def divide(t, scalar):
    return tuple(t[0] / scalar, t[1] / scalar, t[2] / scalar, t[3] / scalar)


def magnitude(v):
    return sqrt(v[0]**2 + v[1]**2 + v[2]**2 + v[3]**2)


def normalize(v):
    m = magnitude(v)
    return divide(v, m)


def dot(t1, t2):
    return t1[0]*t2[0]+ \
           t1[1]*t2[1]+ \
           t1[2]*t2[2]+ \
           t1[3]*t2[3]


def cross(t1, t2):
    return vector(t1[1] * t2[2] - t1[2] * t2[1], t1[2] * t2[0] - t1[0] * t2[2],
                  t1[0] * t2[1] - t1[1] * t2[0])


def hadamard(c1, c2):
    return color(c1[0] * c2[0], c1[1] * c2[1], c1[2] * c2[2])


def reflect(in_vector, normal):
    scalar = 2 * dot(in_vector, normal)
    return subtract(in_vector, multiply(normal, scalar))
