from math import sqrt
from behave import when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple
from tuples import point, vector
from hit import Hit


@when(u'shape_hit <- hit(i1, r)')
def step_assign_hit_i1_r_to_shape_hit(context):
    context.shape_hit = Hit(context.i1, context.r)


@then(u'shape_hit.t = i1.t')
def step_assert_shape_hit_t_equals_i1_t(context):
    assert_float(context.shape_hit.t, context.i1.t)


@then(u'shape_hit.object = i1.object')
def step_assert_shape_hit_object_equals_i1_object(context):
    assert context.shape_hit.object == context.i1.object


@then(u'shape_hit.point = point({x:g}, {y:g}, {z:g})')
def step_assert_shape_hit_point_equals_point(context, x, y, z):
    assert_tuple(context.shape_hit.point, point(x, y, z))


@then(u'shape_hit.eyev = vector({x:g}, {y:g}, {z:g})')
def step_assert_shape_hit_eyev_equals_vector(context, x, y, z):
    assert_tuple(context.shape_hit.eyev, vector(x, y, z))


@then(u'shape_hit.normalv = vector({x:g}, {y:g}, {z:g})')
def step_assert_shape_hit_normalv_equals_vector(context, x, y, z):
    assert_tuple(context.shape_hit.normalv, vector(x, y, z))


@then(u'shape_hit.inside = {expected}')
def step_assert_shape_hit_inside(context, expected):
    assert context.shape_hit.inside == (expected.lower() == "true")


@then(u'shape_hit.reflectv = vector(0, sqrt(2)/2, sqrt(2)/2)')
def step_assert_shape_hit_reflectv_equals_specific_vector(context):
    assert_tuple(context.shape_hit.reflectv, vector(0,
                                                    sqrt(2) / 2,
                                                    sqrt(2) / 2))
