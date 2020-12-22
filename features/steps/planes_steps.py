from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from tuples import point, vector
from plane import Plane


@given(u'p <- plane()')
def step_create_plane_p(context):
    context.p = Plane()


@when(u's <- Plane.from_yaml(data)')
def step_create_plane_s_from_yaml(context):
    context.s = Plane.from_yaml(context.data)


@when(u'n1 <- local_normal_at(p, point({x:g}, {y:g}, {z:g}))')
def step_assign_local_normal_at_to_n1(context, x, y, z):
    context.n1 = context.p.local_normal_at(point(x, y, z))


@when(u'n2 <- local_normal_at(p, point({x:g}, {y:g}, {z:g}))')
def step_assign_local_normal_at_to_n2(context, x, y, z):
    context.n2 = context.p.local_normal_at(point(x, y, z))


@when(u'n3 <- local_normal_at(p, point({x:g}, {y:g}, {z:g}))')
def step_assign_local_normal_at_to_n3(context, x, y, z):
    context.n3 = context.p.local_normal_at(point(x, y, z))


@when(u'xs <- local_intersect(p, r)')
def step_assign_local_intersect_p_r_to_xs(context):
    context.xs = context.p.local_intersect(context.r)


@then(u'n1 = vector({x:g}, {y:g}, {z:g})')
def step_assert_n1_equals_vector(context, x, y, z):
    assert_tuple(context.n1, vector(x, y, z))


@then(u'n2 = vector({x:g}, {y:g}, {z:g})')
def step_assert_n2_equals_vector(context, x, y, z):
    assert_tuple(context.n2, vector(x, y, z))


@then(u'n3 = vector({x:g}, {y:g}, {z:g})')
def step_assert_n3_equals_vector(context, x, y, z):
    assert_tuple(context.n3, vector(x, y, z))


@then(u'xs[{index:d}].object = p')
def step_assert_object_of_xs_at_index_equals_p(context, index):
    actual = context.xs[index].object
    assert actual == context.p, f"{actual} is not {context.p}"
