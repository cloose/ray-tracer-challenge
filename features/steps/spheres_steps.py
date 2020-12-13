from math import sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple
from tuples import point, vector
from shape import Shape
from sphere import Sphere
from matrix import identity_matrix, multiply
from transformations import scaling, rotation_z
from material import Material


@given(u's <- sphere()')
def step_create_sphere_s(context):
    context.s = Sphere()


@when(u'set_transform(s, B)')
def step_set_transform_of_s_to_b(context):
    context.s.set_transform(context.B)


@when(u'set_transform(s, C)')
def step_set_transform_of_s_to_c(context):
    context.s.set_transform(context.C)


@when(u'xs <- local_intersect(s, r)')
def step_assign_local_intersect_s_r_to_xs(context):
    context.xs = context.s.local_intersect(context.r)


@when(u'n <- local_normal_at(s, point({x:g}, {y:g}, {z:g}))')
def step_assign_local_normal_of_s_at_point_to_n(context, x, y, z):
    context.n = context.s.local_normal_at(point(x, y, z))


@when(u'n <- local_normal_at(s, point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))')
def step_assign_local_normal_of_s_at_certain_point_to_n(context):
    xyz = sqrt(3) / 3
    context.n = context.s.local_normal_at(point(xyz, xyz, xyz))


@then(u's is a shape')
def step_impl(context):
    assert isinstance(context.s, Shape)


@then(u'xs is empty')
def step_assert_xs_is_empty(context):
    assert not context.xs


@then(u'xs.count = {expected:d}')
def step_assert_count_of_xs(context, expected):
    actual = len(context.xs)
    assert_float(actual, expected)


@then(u'xs[{index:d}].object = s')
def step_assert_object_of_xs_at_index_equals_s(context, index):
    actual = context.xs[index].object
    assert actual == context.s, f"{actual} is not {context.s}"


@then(u'xs[{index:d}].t = {expected:g}')
def step_assert_t_of_xs_at_index(context, index, expected):
    actual = context.xs[index].t
    assert actual == expected, f"{actual} is not {expected}"


@then(u's.transform = C')
def step_assert_transform_of_s_equals_c(context):
    assert context.s.transform() == context.C


@then(u'n = vector({x:g}, {y:g}, {z:g})')
def step_assert_n_equals_vector(context, x, y, z):
    assert_tuple(context.n, vector(x, y, z))


@then(u'n = vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3)')
def step_assert_n_equals_certain_vector(context):
    xyz = sqrt(3) / 3
    assert_tuple(context.n, vector(xyz, xyz, xyz))
