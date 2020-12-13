from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from lights import PointLight
from tuples import point, color


@given(
    u'light <- point_light(point({px:g}, {py:g}, {pz:g}), color({red:g}, {green:g}, {blue:g}))'
)
def step_create_point_light_direct(context, px, py, pz, red, green, blue):
    context.light = PointLight(point(px, py, pz), color(red, green, blue))


@when(u'light <- point_light(p, c)')
def step_create_point_light(context):
    context.light = PointLight(context.p, context.c)


@then(u'light.position = p')
def step_assert_light_position_equals_p(context):
    assert_tuple(context.light.position, context.p)


@then(u'light.intensity = c')
def step_assert_light_intensity_equals_c(context):
    assert_tuple(context.light.intensity, context.c)
