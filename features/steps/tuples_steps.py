from math import sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple
from core import tuple_4d, point, vector, ispoint, isvector, add, subtract, negate, multiply, divide, magnitude, normalize, dot, cross, reflect


@given(u'a <- tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_create_tuple_a(context, x, y, z, w):
    context.a = tuple_4d(x, y, z, w)


@given(u'a1 <- tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_create_tuple_a1(context, x, y, z, w):
    context.a1 = tuple_4d(x, y, z, w)


@given(u'a2 <- tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_create_tuple_a2(context, x, y, z, w):
    context.a2 = tuple_4d(x, y, z, w)


@given(u'p <- point({x:g}, {y:g}, {z:g})')
def step_create_point_p(context, x, y, z):
    context.p = point(x, y, z)


@given(u'p1 <- point({x:g}, {y:g}, {z:g})')
def step_create_point_p1(context, x, y, z):
    context.p1 = point(x, y, z)


@given(u'p2 <- point({x:g}, {y:g}, {z:g})')
def step_create_point_p2(context, x, y, z):
    context.p2 = point(x, y, z)


@given(u'p3 <- point({x:g}, {y:g}, {z:g})')
def step_create_point_p3(context, x, y, z):
    context.p3 = point(x, y, z)


@given(u'to <- point({x:g}, {y:g}, {z:g})')
def step_create_point_to(context, x, y, z):
    context.to = point(x, y, z)


@given(u'v <- vector({x:g}, {y:g}, {z:g})')
def step_create_vector_v(context, x, y, z):
    context.v = vector(x, y, z)


@given(u'v1 <- vector({x:g}, {y:g}, {z:g})')
def step_create_vector_v1(context, x, y, z):
    context.v1 = vector(x, y, z)


@given(u'v2 <- vector({x:g}, {y:g}, {z:g})')
def step_create_vector_v2(context, x, y, z):
    context.v2 = vector(x, y, z)


@given(u'up <- vector({x:g}, {y:g}, {z:g})')
def step_create_vector_up(context, x, y, z):
    context.up = vector(x, y, z)


@given(u'v2 <- vector(sqrt(2)/2, sqrt(2)/2, 0)')
def step_create_certain_vector_v2(context):
    xyz = sqrt(2) / 2
    context.v2 = vector(xyz, xyz, 0)


@given(u'zero <- vector({x:g}, {y:g}, {z:g})')
def step_create_vector_zero(context, x, y, z):
    context.zero = vector(x, y, z)


@when(u'norm <- normalize(v)')
def step_assign_normalized_v_to_norm(context):
    context.norm = normalize(context.v)


@when(u'r <- reflect(v1, v2)')
def step_assign_reflect_v1_v2_to_r(context):
    context.r = reflect(context.v1, context.v2)


@then(u'a.x = {expected:g}')
def step_assert_x_coordinate_of_a(context, expected):
    assert_float(context.a[0], expected)


@then(u'a.y = {expected:g}')
def step_assert_y_coordinate_of_a(context, expected):
    assert_float(context.a[1], expected)


@then(u'a.z = {expected:g}')
def step_assert_z_coordinate_of_a(context, expected):
    assert_float(context.a[2], expected)


@then(u'a.w = {expected:g}')
def step_assert_w_coordinate_of_a(context, expected):
    assert_float(context.a[3], expected)


@then(u'a is a point')
def step_assert_a_is_point(context):
    assert ispoint(context.a)


@then(u'a is not a point')
def step_assert_a_is_not_point(context):
    assert not ispoint(context.a)


@then(u'a is a vector')
def step_assert_a_is_vector(context):
    assert isvector(context.a)


@then(u'a is not a vector')
def step_assert_a_is_not_vector(context):
    assert not isvector(context.a)


@then(u'p = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_assert_p_equals_tuple(context, x, y, z, w):
    expected = tuple_4d(x, y, z, w)
    assert_tuple(context.p, expected)


@then(u'p2 = point({x:g}, {y:g}, {z:g})')
def step_assert_p2_equals_point(context, x, y, z):
    expected = point(x, y, z)
    assert_tuple(context.p2, expected)


@then(u'p3 = point({x:g}, {y:g}, {z:g})')
def step_assert_p3_equals_point(context, x, y, z):
    expected = point(x, y, z)
    assert_tuple(context.p3, expected)


@then(u'p4 = point({x:g}, {y:g}, {z:g})')
def step_assert_p4_equals_point(context, x, y, z):
    expected = point(x, y, z)
    assert_tuple(context.p4, expected)


@then(u'v = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_assert_v_equals_tuple(context, x, y, z, w):
    expected = tuple_4d(x, y, z, w)
    assert_tuple(context.v, expected)


@then(u'r = vector({x:g}, {y:g}, {z:g})')
def step_assert_r_equals_vector(context, x, y, z):
    expected = vector(x, y, z)
    assert_tuple(context.r, expected)


@then(u'a1 + a2 = tuple(1, 1, 6, 1)')
def step_assert_addition_a1_a2_equals_tuple(context):
    expected = tuple_4d(1, 1, 6, 1)
    assert_tuple(add(context.a1, context.a2), expected)


@then(u'p1 - p2 = vector(-2, -4, -6)')
def step_assert_subtraction_p1_p2_equals_vector(context):
    assert_tuple(subtract(context.p1, context.p2), vector(-2, -4, -6))


@then(u'p - v = point(-2, -4, -6)')
def step_assert_subtraction_p_v_equals_point(context):
    assert_tuple(subtract(context.p, context.v), point(-2, -4, -6))


@then(u'v1 - v2 = vector(-2, -4, -6)')
def step_assert_subtraction_v1_v2_equals_vector(context):
    assert subtract(context.v1, context.v2) == vector(-2, -4, -6)


@then(u'zero - v = vector(-1, 2, -3)')
def step_assert_subtraction_zero_v_equals_vector(context):
    assert subtract(context.zero, context.v) == vector(-1, 2, -3)


@then(u'-a = tuple(-1, 2, -3, 4)')
def step_assert_negated_a_equals_tuple(context):
    assert_tuple(negate(context.a), tuple_4d(-1, 2, -3, 4))


@then(u'a * {s:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, s, x, y, z, w):
    assert multiply(context.a, s) == tuple_4d(x, y, z, w)


@then(u'a / {s:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, s, x, y, z, w):
    assert divide(context.a, s) == tuple_4d(x, y, z, w)


@then(u'magnitude(v) = {expected:g}')
def step_assert_magnitude_of_v(context, expected):
    assert magnitude(context.v) == expected


@then(u'magnitude(v) = sqrt({l:g})')
def step_impl(context, l):
    assert magnitude(context.v) == sqrt(l)


@then(u'normalize(v) = vector(1, 0, 0)')
def step_assert_normalized_v_equals_vector(context):
    assert normalize(context.v) == vector(1, 0, 0)


@then(u'normalize(v) = approximately vector({x:g}, {y:g}, {z:g})')
def step_assert_normalized_v_approx_equals_vector(context, x, y, z):
    norm = normalize(context.v)
    assert_tuple(norm, vector(x, y, z))


@then(u'magnitude(norm) = 1')
def step_assert_magnitude_of_norm(context):
    assert_float(magnitude(context.norm), 1)


@then(u'dot(v1, v2) = {expected:g}')
def step_assert_dot_product_v1_v2(context, expected):
    assert_float(dot(context.v1, context.v2), expected)


@then(u'cross(v1, v2) = vector({x:g}, {y:g}, {z:g})')
def step_assert_cross_product_v1_v2_equals_vector(context, x, y, z):
    actual = cross(context.v1, context.v2)
    expected = vector(x, y, z)
    assert_tuple(actual, expected)


@then(u'cross(v2, v1) = vector({x:g}, {y:g}, {z:g})')
def step_assert_cross_product_v2_v1_equals_vector(context, x, y, z):
    actual = cross(context.v2, context.v1)
    expected = vector(x, y, z)
    assert_tuple(actual, expected)
