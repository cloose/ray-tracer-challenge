from math import sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from tuples import point, vector
from rays import Ray


@given(u'origin <- point({x:g}, {y:g}, {z:g})')
def step_create_point_origin(context, x, y, z):
    context.origin = point(x, y, z)


@given(u'direction <- vector({x:g}, {y:g}, {z:g})')
def step_create_vector_direction(context, x, y, z):
    context.direction = vector(x, y, z)


@given(
    u'r <- ray(point({ox:g}, {oy:g}, {oz:g}), vector({dx:g}, {dy:g}, {dz:g}))')
def step_impl(context, ox, oy, oz, dx, dy, dz):
    context.r = Ray(point(ox, oy, oz), vector(dx, dy, dz))


@when(u'r <- ray(origin, direction)')
def step_impl(context):
    context.r = Ray(context.origin, context.direction)


@when(u'r2 <- transform(r, B)')
def step_impl(context):
    context.r2 = context.r.transformed(context.B)


@when(u'r2 <- transform(r, C)')
def step_impl(context):
    context.r2 = context.r.transformed(context.C)


@then(u'r.origin = origin')
def step_impl(context):
    assert_tuple(context.r.origin, context.origin)


@then(u'r.direction = direction')
def step_impl(context):
    assert_tuple(context.r.direction, context.direction)


@then(u'position(r, {t:g}) = point({x:g}, {y:g}, {z:g})')
def step_impl(context, t, x, y, z):
    actual = context.r.position_at(t)
    expected = point(x, y, z)
    assert_tuple(actual, expected)


@then(u'r2.origin = point({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    actual = context.r2.origin
    expected = point(x, y, z)
    assert_tuple(actual, expected)


@then(u'r2.direction = vector({x:g}, {y:g}, {z:g})')
def step_impl(context, x, y, z):
    actual = context.r2.direction
    expected = vector(x, y, z)
    assert_tuple(actual, expected)


@then(u'r2.direction = vector(sqrt(2)/2, 0, -sqrt(2)/2)')
def step_assert_direction_of_r2_is_certain_vector(context):
    actual = context.r2.direction
    expected = vector(sqrt(2) / 2, 0, -sqrt(2) / 2)
    assert_tuple(actual, expected)
