from math import cos, sin
from tuples import normalize, subtract, cross
from matrix import identity_matrix, multiply


def translation(x, y, z):
    result = identity_matrix()
    result[0][3] = x
    result[1][3] = y
    result[2][3] = z
    return result


def scaling(x, y, z):
    result = identity_matrix()
    result[0][0] = x
    result[1][1] = y
    result[2][2] = z
    return result


def rotation_x(angle):
    result = identity_matrix()
    result[1][1] = cos(angle)
    result[1][2] = -sin(angle)
    result[2][1] = sin(angle)
    result[2][2] = cos(angle)
    return result


def rotation_y(angle):
    result = identity_matrix()
    result[0][0] = cos(angle)
    result[0][2] = sin(angle)
    result[2][0] = -sin(angle)
    result[2][2] = cos(angle)
    return result


def rotation_z(angle):
    result = identity_matrix()
    result[0][0] = cos(angle)
    result[0][1] = -sin(angle)
    result[1][0] = sin(angle)
    result[1][1] = cos(angle)
    return result


def shearing(xy, xz, yx, yz, zx, zy):
    result = identity_matrix()
    result[0][1] = xy
    result[0][2] = xz
    result[1][0] = yx
    result[1][2] = yz
    result[2][0] = zx
    result[2][1] = zy
    return result


def view_transform(from_point, to, up):
    forward_vector = normalize(subtract(to, from_point))
    left_vector = cross(forward_vector, normalize(up))
    true_up = cross(left_vector, forward_vector)

    orientation = identity_matrix()
    orientation[0][0] = left_vector[0]
    orientation[0][1] = left_vector[1]
    orientation[0][2] = left_vector[2]
    orientation[1][0] = true_up[0]
    orientation[1][1] = true_up[1]
    orientation[1][2] = true_up[2]
    orientation[2][0] = -forward_vector[0]
    orientation[2][1] = -forward_vector[1]
    orientation[2][2] = -forward_vector[2]

    return multiply(
        orientation, translation(-from_point[0], -from_point[1],
                                 -from_point[2]))
