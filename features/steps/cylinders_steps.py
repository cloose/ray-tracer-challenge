import math
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple, assert_matrix
from core import color, translation
from shapes import Cylinder


@given(u'c <- cylinder()')
def step_create_cylinder_c(context):
    context.c = Cylinder()


@given(u'c.minimum <- {expected:g}')
def step_set_minimum_of_cylinder_c(context, expected):
    context.c.minimum = expected


@given(u'c.maximum <- {expected:g}')
def step_set_maximum_of_cylinder_c(context, expected):
    context.c.maximum = expected


@given(u'c.closed <- {expected}')
def step_set_closed_of_cylinder_c(context, expected):
    context.c.closed = (expected.lower() == "true")


@when(u'c <- Cylinder.from_yaml(data)')
def step_create_cylinder_c_from_yaml(context):
    context.c = Cylinder.from_yaml(context.data)


@then(u'c.maximum = {expected}')
def step_assert_maximum_of_cylinder_c(context, expected):
    if isinstance(expected, str) and expected == 'infinity':
        assert context.c.maximum == math.inf, \
                f"{context.c.maximum} is not infinity"
    else:
        assert_float(context.c.maximum, float(expected))


@then(u'c.minimum = {expected}')
def step_assert_minimum_of_cylinder_c(context, expected):
    if isinstance(expected, str) and expected == '-infinity':
        assert context.c.minimum == -math.inf, \
                f"{context.c.minimum} is not -infinity"
    else:
        assert_float(context.c.minimum, float(expected))


@then(u'c.closed = {expected}')
def step_assert_closed_of_cylinder_c(context, expected):
    assert context.c.closed == (expected.lower() == "true"), \
        f"{context.c.closed} is not {expected.lower()}"


@then(u'c.transform = translation({x:g}, {y:g}, {z:g})')
def step_assert_transform_of_c_equals_translation_matrix(context, x, y, z):
    assert_matrix(context.c.transform(), translation(x, y, z))


@then(u'c.material.color = color({red:g}, {green:g}, {blue:g})')
def step_assert_color_of_material(context, red, green, blue):
    assert_tuple(context.c.material.color, color(red, green, blue))
