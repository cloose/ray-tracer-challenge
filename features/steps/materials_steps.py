from math import sqrt

from behave import given, then, when  # pylint: disable=no-name-in-module

from asserts import assert_float, assert_tuple
from core import color, lighting, normalize, point, subtract, vector
from patterns import (CheckersPattern, GradientPattern, RingPattern,
                      StripePattern)
from shapes import Material


@given(u'm <- material()')
def step_create_default_material_m(context):
    context.m = Material()


@given(u'm.ambient <- {value:g}')
def step_set_ambient_of_m(context, value):
    context.m.ambient = value


@given(u'm.diffuse <- {value:g}')
def step_set_diffuse_of_m(context, value):
    context.m.diffuse = value


@given(u'm.specular <- {value:g}')
def step_set_specular_of_m(context, value):
    context.m.specular = value


@given(u'm.color <- color({red:g}, {green:g}, {blue:g})')
def step_set_color_of_m(context, red, green, blue):
    context.m.color = color(red, green, blue)


@given(u'm.pattern <- stripe_pattern(color(1, 1, 1), color(0, 0, 0))')
def step_set_pattern_of_m(context):
    context.m.pattern = StripePattern(color(1, 1, 1), color(0, 0, 0))


@given(u'v1 <- vector(0, sqrt(2)/2, -sqrt(2)/2)')
def step_create_vector_v1_eye_offset_45(context):
    context.v1 = vector(0, sqrt(2) / 2, -sqrt(2) / 2)


@given(u'v1 <- vector(0, -sqrt(2)/2, -sqrt(2)/2)')
def step_create_vector_v1_reflection(context):
    context.v1 = vector(0, -sqrt(2) / 2, -sqrt(2) / 2)


@given(u'v1 <- normalize(eye - p)')
def step_create_eye_vector_v1_from_eye_to_p(context):
    context.v1 = normalize(subtract(context.eye, context.p))


@given(u'v2 <- vector(p.x, p.y, p.z)')
def step_create_normal_vector_v2_from_point(context):
    context.v2 = vector(context.p[0], context.p[1], context.p[2])


@when(u'm <- Material.from_yaml(data)')
def step_create_material_m_from_yaml(context):
    context.m = Material.from_yaml(context.data)


@when(u'c <- lighting(m, s, light, p, v1, v2)')
def step_set_c_to_calculated_lighting_with_default_intensity(context):
    context.c = lighting(context.m, context.s, context.light, context.p,
                         context.v1, context.v2, 1.0)


@when(
    u'c <- lighting(m, {shape_var}, light, {point_var}, v1, v2, {intensity:g})'
)
def step_set_c_to_calculated_lighting(context, shape_var, point_var,
                                      intensity):
    shape = getattr(context, shape_var)
    p = getattr(context, point_var)
    context.c = lighting(context.m, shape, context.light, p, context.v1,
                         context.v2, intensity)


@when(
    u'c2 <- lighting(m, {shape_var}, light, {point_var}, v1, v2, {intensity:g})'
)
def step_set_c2_to_calculated_lighting(context, shape_var, point_var,
                                       intensity):
    shape = getattr(context, shape_var)
    p = getattr(context, point_var)
    context.c2 = lighting(context.m, shape, context.light, p, context.v1,
                          context.v2, intensity)


@then(u'm.color = color({red:g}, {green:g}, {blue:g})')
def step_assert_color_of_m(context, red, green, blue):
    assert_tuple(context.m.color, color(red, green, blue))


@then(u'm.ambient = {expected:g}')
def step_assert_ambient_of_m(context, expected):
    assert_float(context.m.ambient, expected)


@then(u'm.diffuse = {expected:g}')
def step_assert_diffuse_of_m(context, expected):
    assert_float(context.m.diffuse, expected)


@then(u'm.specular = {expected:g}')
def step_assert_specular_of_m(context, expected):
    assert_float(context.m.specular, expected)


@then(u'm.shininess = {expected:g}')
def step_assert_shininess_of_m(context, expected):
    assert_float(context.m.shininess, expected)


@then(u'm.reflective = {expected:g}')
def step_assert_reflective_of_m(context, expected):
    assert_float(context.m.reflective, expected)


@then(u'm.transparency = {expected:g}')
def step_assert_transparency_of_m(context, expected):
    assert_float(context.m.transparency, expected)


@then(u'm.refractive_index = {expected:g}')
def step_assert_refractive_index_of_m(context, expected):
    assert_float(context.m.refractive_index, expected)


@then(u'c1 = color({red:g}, {green:g}, {blue:g})')
def step_assert_color_of_c1(context, red, green, blue):
    assert_tuple(context.c1, color(red, green, blue))


@then(u'c2 = color({red:g}, {green:g}, {blue:g})')
def step_assert_color_of_c2(context, red, green, blue):
    assert_tuple(context.c2, color(red, green, blue))


@then(u'm.pattern = stripe_pattern(color(1, 1, 1), color(0, 0, 0))')
def step_assert_pattern_of_m_is_stripe_pattern(context):
    assert isinstance(context.m.pattern, StripePattern), \
        f"{context.m.pattern.__class__.__name__} is not StripePattern"
    assert_tuple(context.m.pattern.color_a, color(1, 1, 1))
    assert_tuple(context.m.pattern.color_b, color(0, 0, 0))


@then(u'm.pattern = checkers_pattern(color(1, 1, 1), color(0, 0, 0))')
def step_assert_pattern_of_m_is_checkers_pattern(context):
    assert isinstance(context.m.pattern, CheckersPattern), \
        f"{context.m.pattern.__class__.__name__} is not CheckersPattern"
    assert_tuple(context.m.pattern.color_a, color(1, 1, 1))
    assert_tuple(context.m.pattern.color_b, color(0, 0, 0))


@then(u'm.pattern = ring_pattern(color(1, 1, 1), color(0, 0, 0))')
def step_assert_pattern_of_m_is_ring_pattern(context):
    assert isinstance(context.m.pattern, RingPattern), \
        f"{context.m.pattern.__class__.__name__} is not RingPattern"
    assert_tuple(context.m.pattern.color_a, color(1, 1, 1))
    assert_tuple(context.m.pattern.color_b, color(0, 0, 0))


@then(u'm.pattern = gradient_pattern(color(1, 1, 1), color(0, 0, 0))')
def step_assert_pattern_of_m_is_gradient_pattern(context):
    assert isinstance(context.m.pattern, GradientPattern), \
        f"{context.m.pattern.__class__.__name__} is not GradientPattern"
    assert_tuple(context.m.pattern.color_a, color(1, 1, 1))
    assert_tuple(context.m.pattern.color_b, color(0, 0, 0))
