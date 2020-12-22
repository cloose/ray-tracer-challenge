from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from tuples import vector
from shape import Cube


@given(u'c <- cube()')
def step_create_cube_c(context):
    context.c = Cube()


@when(u'xs <- local_intersect(c, r)')
def step_assign_local_intersect_between_cube_and_ray_to_xs(context):
    context.xs = context.c.local_intersect(context.r)


@when(u'normal <- local_normal_at(c, p)')
def step_assign_local_normal_for_cube_at_point_to_normal(context):
    context.normal = context.c.local_normal_at(context.p)


@then(u'normal = vector({x:g}, {y:g}, {z:g})')
def step_assert_normal_equals_vector(context, x, y, z):
    assert_tuple(context.normal, vector(x, y, z))
