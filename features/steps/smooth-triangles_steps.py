from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple
from core import point, vector
from shapes import Triangle


@given(u'n1 <- vector(0, 1, 0)')
def step_create_normal_vector_n1(context):
    context.n1 = vector(0, 1, 0)


@given(u'n2 <- vector(-1, 0, 0)')
def step_create_normal_vector_n2(context):
    context.n2 = vector(-1, 0, 0)


@given(u'n3 <- vector(1, 0, 0)')
def step_create_normal_vector_n3(context):
    context.n3 = vector(1, 0, 0)


@when(u'tri <- smooth_triangle(p1, p2, p3, n1, n2, n3)')
def step_create_smooth_triangle_tri(context):
    context.tri = Triangle.smooth_triangle(context.p1, context.p2, context.p3,
                                           context.n1, context.n2, context.n3)


@when(u'xs <- local_intersect(tri, r)')
def step_assign_local_intersect_of_tri_with_r_to_xs(context):
    context.xs = context.tri.local_intersect(context.r)


@when(u'n <- normal_at(tri, point(0, 0, 0), i)')
def step_assign_normal_of_tri_at_point_to_i(context):
    context.n = context.tri.normal_at(point(0, 0, 0), context.i)


@then(u'tri.{var_name} = {var_name}')
def step_assert_attribute_of_smooth_triangle(context, var_name):
    actual = getattr(context.tri, var_name, None)
    expected = getattr(context, var_name, None)
    assert_tuple(actual, expected)


@then(u'xs[{index:d}].{var_name} = {expected:g}')
def step_assert_attribute_of_intersection_at_index(context, index, var_name,
                                                   expected):
    actual = getattr(context.xs[index], var_name, None)
    assert_float(actual, expected)
