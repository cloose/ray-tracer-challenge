from math import sqrt
from behave import when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple
from tuples import point, vector
from hit import Hit

_EPSILON = 0.00001


@when(u'shape_hit <- hit(i1, r)')
def step_assign_hit_i1_r_to_shape_hit(context):
    context.shape_hit = Hit(context.i1, context.r)


@when(u'shape_hit <- hit(xs[{index:d}], r, xs)')
def step_assign_hit_at_index_r_to_shape_hit(context, index):
    context.shape_hit = Hit(context.xs[index], context.r, context.xs)


@when(u'shape_hit <- hit(i1, r, xs)')
def step_assign_hit_at_i1_r_to_shape_hit(context):
    context.shape_hit = Hit(context.i1, context.r, context.xs)


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


@then(u'shape_hit.over_point.z < -EPSILON/2')
def step_assert_over_point_z_less_than_negative_half_epsilon(context):
    assert context.shape_hit.over_point[2] < -(_EPSILON / 2), \
            f"{context.shape_hit.over_point[2]} is not less than {-(_EPSILON/2)}"


@then(u'shape_hit.point.z > shape_hit.over_point.z')
def step_assert_point_z_greater_than_over_point_z(context):
    assert context.shape_hit.point[2] > context.shape_hit.over_point[2]


@then(u'shape_hit.under_point.z > EPSILON/2')
def step_assert_under_point_z_greater_than_half_epsilon(context):
    assert context.shape_hit.under_point[2] > (_EPSILON / 2), \
            f"{context.shape_hit.under_point[2]} is not greater than {(_EPSILON/2)}"


@then(u'shape_hit.point.z < shape_hit.under_point.z')
def step_assert_point_z_less_than_under_point_z(context):
    assert context.shape_hit.point[2] < context.shape_hit.under_point[2]


@then(u'shape_hit.n1 = {expected:g}')
def step_assert_shape_hit_n1(context, expected):
    assert_float(context.shape_hit.n1, expected)


@then(u'shape_hit.n2 = {expected:g}')
def step_assert_shape_hit_n2(context, expected):
    assert_float(context.shape_hit.n2, expected)
