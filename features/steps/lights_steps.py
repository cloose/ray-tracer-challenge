from behave import given, then, when  # pylint: disable=no-name-in-module

from asserts import assert_float, assert_tuple
from core import DeterministicSequence, color, point, vector
from lights import AreaLight, PointLight


@given(
    u'light <- point_light(point({px:g}, {py:g}, {pz:g}), color({red:g}, {green:g}, {blue:g}))'
)
def step_create_point_light_direct(context, px, py, pz, red, green, blue):
    context.light = PointLight(point(px, py, pz), color(red, green, blue))


@given(
    u'light <- area_light(corner, v1, {vsteps:d}, v2, {usteps:d}, color({red:g}, {green:g}, {blue:g}))'
)
def step_create_area_light(context, vsteps, usteps, red, green, blue):
    context.light = AreaLight(context.corner, context.v1, vsteps, context.v2,
                              usteps, color(red, green, blue))


@given(u'light.jitter_by <- sequence({values})')
def step_set_jitter_by_of_light_to_sequence(context, values):
    value_list = [float(x.strip()) for x in values.split(',')]
    context.light.jitter_by = DeterministicSequence(value_list)


@when(u'light <- point_light(p, c)')
def step_create_point_light(context):
    context.light = PointLight(context.p, context.c)


@when(u'light <- PointLight.from_yaml(data)')
def step_create_point_light_from_yaml(context):
    context.light = PointLight.from_yaml(context.data)


@when(
    u'light <- area_light(corner, v1, {vsteps:d}, v2, {usteps:d}, color({red:g}, {green:g}, {blue:g}))'
)
def step_set_light_to_area_light(context, vsteps, usteps, red, green, blue):
    context.light = AreaLight(context.corner, context.v1, vsteps, context.v2,
                              usteps, color(red, green, blue))


@when(u'light <- AreaLight.from_yaml(data)')
def step_create_area_light_from_yaml(context):
    context.light = AreaLight.from_yaml(context.data)


@when(u'intensity <- intensity_at(light, p, w)')
def step_assign_intensity_to_calculated_intensity_at_point(context):
    context.intensity = context.light.intensity_at(context.p, context.w)


@when(u'p <- point_on_light(light, {u:d}, {v:d})')
def step_assign_point_on_light_to_p(context, u, v):
    context.p = context.light.point_on_light(u, v)


@then(u'light.position = p')
def step_assert_light_position_equals_p(context):
    assert_tuple(context.light.position, context.p)


@then(u'light.intensity = c')
def step_assert_light_intensity_equals_c(context):
    assert_tuple(context.light.intensity, context.c)


@then(u'light.position = point({x:g}, {y:g}, {z:g})')
def step_assert_light_positon_equals_point(context, x, y, z):
    assert_tuple(context.light.position, point(x, y, z))


@then(u'light.intensity = color({red:g}, {green:g}, {blue:g})')
def step_assert_light_intensity_equals_color(context, red, green, blue):
    assert_tuple(context.light.intensity, color(red, green, blue))


@then(u'intensity = {expected:g}')
def step_assert_intensity_equals_expected(context, expected):
    assert_float(context.intensity, expected)


@then(u'light.corner = point({x:g}, {y:g}, {z:g})')
def step_assert_light_corner_equals_point(context, x, y, z):
    assert_tuple(context.light.corner, point(x, y, z))


@then(u'light.corner = corner')
def step_assert_light_corner_equals_corner(context):
    assert_tuple(context.light.corner, context.corner)


@then(u'light.uvec = vector({x:g}, {y:g}, {z:g})')
def step_assert_light_uvec_equals_vector(context, x, y, z):
    assert_tuple(context.light.uvec, vector(x, y, z))


@then(u'light.usteps = {expected:d}')
def step_assert_light_ustep_equals_expected(context, expected):
    assert context.light.usteps == expected


@then(u'light.vvec = vector({x:g}, {y:g}, {z:g})')
def step_assert_light_vvec_equals_vector(context, x, y, z):
    assert_tuple(context.light.vvec, vector(x, y, z))


@then(u'light.vsteps = {expected:d}')
def step_assert_light_vstep_equals_expected(context, expected):
    assert context.light.vsteps == expected


@then(u'light.samples = {expected:d}')
def step_assert_light_samples_equals_expected(context, expected):
    assert context.light.samples == expected
