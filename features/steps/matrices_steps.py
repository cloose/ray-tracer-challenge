from tuples import tuple
from math import isclose
from matrix import matrix, multiply, multiply_tuple, identity_matrix, transpose, determinant, submatrix, minor, cofactor, isinvertible, inverse


@given(u'the following {m:d}x{n:d} matrix M')
def step_impl(context, m, n):
    context.m = matrix(m, n)
    for row in range(m):
        for col in range(n):
            context.m[row][col] = float(context.table[row][col])


@given(u'the following matrix A')
def step_impl(context):
    context.a = matrix(4, 4)
    for row in range(4):
        for col in range(4):
            context.a[row][col] = float(context.table[row][col])


@given(u'the following matrix B')
def step_impl(context):
    context.b = matrix(4, 4)
    for row in range(4):
        for col in range(4):
            context.b[row][col] = float(context.table[row][col])


@given(u'b <- tuple({x:d}, {y:d}, {z:d}, {w:d})')
def step_impl(context, x, y, z, w):
    context.b = tuple(x, y, z, w)


@given(u'A <- transpose(identity_matrix)')
def step_impl(context):
    context.a = transpose(identity_matrix())


@when(u'B <- inverse(M)')
def step_impl(context):
    context.b = inverse(context.m)


@when(u'C <- M * B')
def step_impl(context):
    context.c = multiply(context.m, context.b)


@then(u'M[{r:d},{c:d}] = {v:g}')
def step_impl(context, r, c, v):
    context.m[r][c] == v


@then(u'A = B')
def step_impl(context):
    assert context.a == context.b


@then(u'A = identity_matrix')
def step_impl(context):
    assert context.a == identity_matrix()


@then(u'A != B')
def step_impl(context):
    assert context.a != context.b


@then(u'A * B is the following 4x4 matrix')
def step_impl(context):
    expected = matrix(4, 4)
    for r in range(4):
        for c in range(4):
            expected[r][c] = float(context.table[r][c])
    assert multiply(context.a, context.b) == expected


@then(u'transpose(A) is the following matrix')
def step_impl(context):
    expected = matrix(4, 4)
    for r in range(4):
        for c in range(4):
            expected[r][c] = float(context.table[r][c])
    assert transpose(context.a) == expected


@then(u'A * b = tuple(18, 24, 33, 1)')
def step_impl(context):
    assert multiply_tuple(context.a, context.b) == tuple(18, 24, 33, 1)


@then(u'A * identity_matrix = A')
def step_impl(context):
    assert multiply(context.a, identity_matrix()) == context.a


@then(u'identity_matrix * a = a')
def step_impl(context):
    assert multiply_tuple(identity_matrix(), context.a) == context.a


@then(u'determinant(M) = {val:d}')
def step_impl(context, val):
    actual = determinant(context.m)
    assert actual == val, "%r is not %r" % (actual, val)


@then(u'submatrix(M, {r:d}, {c:d}) is the following 2x2 matrix')
def step_impl(context, r, c):
    expected = matrix(2, 2)
    for row in range(2):
        for col in range(2):
            expected[row][col] = float(context.table[row][col])
    actual = submatrix(context.m, r, c)
    assert actual == expected, "%r is not %r" % (actual, expected)


@given(u'B <- submatrix(M, 1, 0)')
def step_impl(context):
    context.b = submatrix(context.m, 1, 0)


@then(u'determinant(B) = 25')
def step_impl(context):
    assert determinant(context.b) == 25


@then(u'minor(M, {row:d}, {col:d}) = {val:g}')
def step_impl(context, row, col, val):
    assert minor(context.m, row, col) == val


@then(u'cofactor(M, {row:d}, {col:d}) = {val:g}')
def step_impl(context, row, col, val):
    actual = cofactor(context.m, row, col)
    assert actual == val, "%r is not %r" % (actual, val)


@then(u'M is invertible')
def step_impl(context):
    assert isinvertible(context.m)


@then(u'M is not invertible')
def step_impl(context):
    assert not isinvertible(context.m)


@then(u'B[{row:d},{col:d}] = {d1:d}/{d2:d}')
def step_impl(context, row, col, d1, d2):
    actual = context.b[row][col]
    expected = d1 / d2
    assert actual == expected, "%r is not %r" % (actual, expected)


@then(u'C * inverse(B) = M')
def step_impl(context):
    actual = multiply(context.c, inverse(context.b))
    expected = context.m
    assert_matrix(actual, expected)


@then(u'B is the following 4x4 matrix')
def step_impl(context):
    expected = matrix(4, 4)
    for row in range(4):
        for col in range(4):
            expected[row][col] = float(context.table[row][col])
    actual = context.b
    assert_matrix(actual, expected)


def assert_matrix(actual, expected):
    rows = len(actual)
    columns = len(actual[0])

    for row in range(rows):
        for col in range(columns):
            assert equal(actual[row][col], expected[row][col]), \
                    "error [%r][%r]: %r is not %r" % (row, col, actual, expected)


EPSILON = 0.00001


def equal(a: float, b: float) -> bool:
    return abs(a - b) < EPSILON
