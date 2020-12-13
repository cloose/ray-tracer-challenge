from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from tuples import color, point
from patterns import StripePattern
from transformations import scaling, translation

COLORS = {'black': color(0, 0, 0), 'white': color(1, 1, 1)}


@given(u'black <- color(0, 0, 0)')
def step_create_color_black(context):
    context.black = color(0, 0, 0)


@given(u'white <- color(1, 1, 1)')
def step_create_color_white(context):
    context.white = color(1, 1, 1)


@given(u'pattern <- stripe_pattern(white, black)')
def step_create_stripe_pattern_pattern(context):
    context.pattern = StripePattern(context.white, context.black)


@given(u'set_transform(s, scaling({x:g}, {y:g}, {z:g}))')
def step_set_transform_of_s_to_scaling_matrix(context, x, y, z):
    context.s.set_transform(scaling(x, y, z))


@given(u'set_pattern_transform(pattern, scaling({x:g}, {y:g}, {z:g}))')
def step_set_transform_of_pattern_to_scaling_matrix(context, x, y, z):
    context.pattern.set_transform(scaling(x, y, z))


@given(u'set_pattern_transform(pattern, translation({x:g}, {y:g}, {z:g}))')
def step_set_transform_of_pattern_to_translation_matrix(context, x, y, z):
    context.pattern.set_transform(translation(x, y, z))


@when(u'c <- stripe_at_object(pattern, s, point({x:g}, {y:g}, {z:g}))')
def step_set_c_to_color_of_stripe_at_point(context, x, y, z):
    context.c = context.pattern.pattern_at_shape(context.s, point(x, y, z))


@then(u'pattern.a = white')
def step_assert_color_a_of_pattern_equals_white(context):
    assert_tuple(context.pattern.color_a, context.white)


@then(u'pattern.b = black')
def step_assert_color_b_of_pattern_equals_black(context):
    assert_tuple(context.pattern.color_b, context.black)


@then(u'stripe_at(pattern, point({x:g}, {y:g}, {z:g})) = {expected_color}')
def step_assert_pattern_at_point_equals_color(context, x, y, z,
                                              expected_color):
    actual = context.pattern.pattern_at(point(x, y, z))
    expected = COLORS.get(expected_color)
    assert_tuple(actual, expected)


@then(u'c = white')
def step_assert_color_c_equals_white(context):
    assert_tuple(context.c, context.white)
