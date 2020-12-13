from math import isclose
from behave import given, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from tuples import color, add, subtract, multiply, hadamard


@given(u'c <- color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    context.c = color(r, g, b)


@given(u'c1 <- color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    context.c1 = color(r, g, b)


@given(u'c2 <- color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    context.c2 = color(r, g, b)


@given(u'c3 <- color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    context.c3 = color(r, g, b)


@then(u'c.red = -0.5')
def step_impl(context):
    assert context.c[0] == -0.5


@then(u'c.green = 0.4')
def step_impl(context):
    assert context.c[1] == 0.4


@then(u'c.blue = 1.7')
def step_impl(context):
    assert context.c[2] == 1.7


@then(u'c = color({red:g}, {green:g}, {blue:g})')
def step_assert_c_equals_color(context, red, green, blue):
    assert_tuple(context.c, color(red, green, blue))


@then(u'c1 + c2 = color(1.6, 0.7, 1.0)')
def step_impl(context):
    assert add(context.c1, context.c2) == color(1.6, 0.7, 1.0)


@then(u'c1 - c2 = color(0.2, 0.5, 0.5)')
def step_impl(context):
    actual = subtract(context.c1, context.c2)
    assert_color(actual, color(0.2, 0.5, 0.5))


@then(u'c * 2 = color(0.4, 0.6, 0.8)')
def step_impl(context):
    assert multiply(context.c, 2) == color(0.4, 0.6, 0.8)


@then(u'c1 * c2 = color(0.9, 0.2, 0.04)')
def step_impl(context):
    assert_color(hadamard(context.c1, context.c2), color(0.9, 0.2, 0.04))


def assert_color(actual, expected):
    assert isclose(actual[0], expected[0])
    assert isclose(actual[1], expected[1])
    assert isclose(actual[2], expected[2])
