from math import sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple
from tuples import point
from material import Material, lighting
from patterns import StripePattern
from tuples import color, vector


@given(u'm <- material()')
def step_create_default_material_m(context):
    context.m = Material()


@given(u'm.ambient <- 1')
def step_set_ambient_of_m(context):
    context.m.ambient = 1


@given(u'm.diffuse <- 0')
def step_set_diffuse_of_m(context):
    context.m.diffuse = 0


@given(u'm.specular <- 0')
def step_set_specular_of_m(context):
    context.m.specular = 0


@given(u'm.pattern <- stripe_pattern(color(1, 1, 1), color(0, 0, 0))')
def step_set_pattern_of_m(context):
    context.m.pattern = StripePattern(color(1, 1, 1), color(0, 0, 0))


@given(u'v1 <- vector(0, sqrt(2)/2, -sqrt(2)/2)')
def step_create_vector_v1_eye_offset_45(context):
    context.v1 = vector(0, sqrt(2) / 2, -sqrt(2) / 2)


@given(u'v1 <- vector(0, -sqrt(2)/2, -sqrt(2)/2)')
def step_create_vector_v1_reflection(context):
    context.v1 = vector(0, -sqrt(2) / 2, -sqrt(2) / 2)


@when(u'c <- lighting(m, s, light, p, v1, v2)')
def step_set_c_to_calculated_lighting(context):
    context.c = lighting(context.m, context.s, context.light, context.p,
                         context.v1, context.v2)


@when(u'c <- lighting(m, s, light, p, v1, v2, in_shadow)')
def step_set_c_to_calculated_lighting_incl_shadow(context):
    context.c = lighting(context.m, context.s, context.light, context.p,
                         context.v1, context.v2, True)


@when(u'c1 <- lighting(m, s, light, point(0.9, 0, 0), v1, v2, false)')
def step_set_c1_to_calculated_lighting(context):
    context.c1 = lighting(context.m, context.s, context.light,
                          point(0.9, 0, 0), context.v1, context.v2, False)


@when(u'c2 <- lighting(m, s, light, point(1.1, 0, 0), v1, v2, false)')
def step_set_c2_to_calculated_lighting(context):
    context.c2 = lighting(context.m, context.s, context.light,
                          point(1.1, 0, 0), context.v1, context.v2, False)


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
