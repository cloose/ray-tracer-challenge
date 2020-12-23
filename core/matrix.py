from copy import deepcopy
from .tuples import tuple_4d


def matrix(rows, columns):
    return [[0.0] * columns for r in range(rows)]


def identity_matrix():
    result = matrix(4, 4)
    for i in range(4):
        result[i][i] = 1
    return result


def submatrix(m, row, column):
    result = deepcopy(m)
    del result[row]
    for row in result:
        del row[column]
    return result


def multiply_matrix(m1, m2):
    rows = len(m1)
    columns = len(m1[0])
    result = matrix(rows, columns)

    for row in range(rows):
        for col in range(columns):
            result[row][col] = m1[row][0] * m2[0][col] + \
                               m1[row][1] * m2[1][col] + \
                               m1[row][2] * m2[2][col] + \
                               m1[row][3] * m2[3][col]

    return result


def multiply_tuple(m, t):
    result = tuple_4d(0, 0, 0, 0)

    for row in range(4):
        result[row] = m[row][0] * t[0] + \
                      m[row][1] * t[1] + \
                      m[row][2] * t[2] + \
                      m[row][3] * t[3]

    return result


def transpose(m):
    rows = len(m)
    columns = len(m[0])
    result = matrix(rows, columns)

    for row in range(rows):
        for col in range(columns):
            result[row][col] = m[col][row]

    return result


def determinant(m):
    result = 0

    if len(m) == 2:
        result = m[0][0] * m[1][1] - \
                 m[0][1] * m[1][0]
    else:
        for column in range(len(m)):
            result = result + m[0][column] * cofactor(m, 0, column)

    return result


def minor(m, row, column):
    sub = submatrix(m, row, column)
    return determinant(sub)


def cofactor(m, row, column):
    result = minor(m, row, column)
    if (row + column) % 2 == 1:
        result = -result
    return result


def isinvertible(m):
    return determinant(m) != 0


def inverse(m):
    # should fail if not invertible
    rows = len(m)
    columns = len(m[0])
    result = matrix(rows, columns)

    det = determinant(m)
    for row in range(rows):
        for col in range(columns):
            c = cofactor(m, row, col)
            result[col][row] = c / det

    return result
