from math import pi, sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from tuples import point, vector
from matrix import multiply, multiply_tuple, inverse
from transformations import translation, scaling, rotation_x, rotation_y, rotation_z, shearing, view_transform


@given(u'transform <- translation(5, -3, 2)')
def step_impl(context):
    context.transform = translation(5, -3, 2)


@given(u'C <- translation({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.C = translation(x, y, z)


@given(u'transform <- scaling({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.transform = scaling(x, y, z)


@given(u'B <- scaling({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    context.B = scaling(x, y, z)


@given(u'transform <- shearing({xy:g}, {xz:g}, {yx:g}, {yz:g}, {zx:g}, {zy:g})'
       )
def step_impl(context, xy, xz, yx, yz, zx, zy):
    context.transform = shearing(xy, xz, yx, yz, zx, zy)


@given(u'transform <- inverse(scaling(2, 3, 4))')
def step_impl(context):
    context.transform = inverse(scaling(2, 3, 4))


@given(u'half_quarter <- rotation_x(pi / 4)')
def step_impl(context):
    context.half_quarter = rotation_x(pi / 4)


@given(u'full_quarter <- rotation_x(pi / 2)')
def step_impl(context):
    context.full_quarter = rotation_x(pi / 2)


@given(u'half_quarter <- rotation_y(pi / 4)')
def step_impl(context):
    context.half_quarter = rotation_y(pi / 4)


@given(u'full_quarter <- rotation_y(pi / 2)')
def step_impl(context):
    context.full_quarter = rotation_y(pi / 2)


@given(u'half_quarter <- rotation_z(pi / 4)')
def step_impl(context):
    context.half_quarter = rotation_z(pi / 4)


@given(u'full_quarter <- rotation_z(pi / 2)')
def step_impl(context):
    context.full_quarter = rotation_z(pi / 2)


@given(u'inv <- inverse(half_quarter)')
def step_impl(context):
    context.inv = inverse(context.half_quarter)


@when(u'p2 <- full_quarter * p')
def step_impl(context):
    context.p2 = multiply_tuple(context.full_quarter, context.p)


@when(u'p3 <- B * p2')
def step_impl(context):
    context.p3 = multiply_tuple(context.B, context.p2)


@when(u'p4 <- C * p3')
def step_impl(context):
    context.p4 = multiply_tuple(context.C, context.p3)


@when(u'transform <- C * B * full_quarter')
def step_impl(context):
    context.transform = multiply(context.C,
                                 multiply(context.B, context.full_quarter))


@when(u'A <- view_transform(p, to, up)')
def step_set_a_to_view_transform_p_to_up(context):
    context.a = view_transform(context.p, context.to, context.up)


@when(u'B <- view_transform(p, to, up)')
def step_set_b_to_view_transform_p_to_up(context):
    context.b = view_transform(context.p, context.to, context.up)


@then(u'transform * p = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    actual = multiply_tuple(context.transform, context.p)
    expected = point(x, y, z)
    assert actual == expected, "%r is not %r" % (actual, expected)


@then(u'transform * v = v')
def step_impl(context):
    actual = multiply_tuple(context.transform, context.v)
    expected = context.v
    assert actual == expected, "%r is not %r" % (actual, expected)


@then(u'transform * v = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    actual = multiply_tuple(context.transform, context.v)
    expected = vector(x, y, z)
    assert actual == expected, "%r is not %r" % (actual, expected)


@then(u'half_quarter * p = point(0, sqrt(2)/2, sqrt(2)/2)')
def step_impl(context):
    actual = multiply_tuple(context.half_quarter, context.p)
    expected = point(0, sqrt(2) / 2, sqrt(2) / 2)
    assert_tuple(actual, expected)


@then(u'half_quarter * p = point(sqrt(2)/2, 0, sqrt(2)/2)')
def step_impl(context):
    actual = multiply_tuple(context.half_quarter, context.p)
    expected = point(sqrt(2) / 2, 0, sqrt(2) / 2)
    assert_tuple(actual, expected)


@then(u'half_quarter * p = point(-sqrt(2)/2, sqrt(2)/2, 0)')
def step_impl(context):
    actual = multiply_tuple(context.half_quarter, context.p)
    expected = point(-sqrt(2) / 2, sqrt(2) / 2, 0)
    assert_tuple(actual, expected)


@then(u'inv * p = point(0, sqrt(2)/2, -sqrt(2)/2)')
def step_impl(context):
    actual = multiply_tuple(context.inv, context.p)
    expected = point(0, sqrt(2) / 2, -sqrt(2) / 2)


@then(u'full_quarter * p = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    actual = multiply_tuple(context.full_quarter, context.p)
    expected = point(x, y, z)
    assert_tuple(actual, expected)


@then(u'A = scaling(-1, 1, -1)')
def step_assert_a_equals_scaling_matrix(context):
    expected = scaling(-1, 1, -1)
    assert context.a == expected, f"{context.a} is not {expected}"


@then(u'A = translation(0, 0, -8)')
def step_assert_a_equals_translation_matrix(context):
    expected = translation(0, 0, -8)
    assert context.a == expected, f"{context.a} is not {expected}"
