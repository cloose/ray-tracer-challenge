from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from core import point, vector
from shapes import Triangle


@given(u't <- triangle(p1, p2, p3)')
def step_create_triangle_t(context):
    context.t = Triangle(context.p1, context.p2, context.p3)


@given(
    u't <- triangle(point({x1:g}, {y1:g}, {z1:g}), point({x2:g}, {y2:g}, {z2:g}), point({x3:g}, {y3:g}, {z3:g}))'
)
def step_create_triangle_t_with_points(context, x1, y1, z1, \
                                                x2, y2, z2, \
                                                x3, y3, z3):
    context.t = Triangle(point(x1, y1, z1), point(x2, y2, z2),
                         point(x3, y3, z3))


@when(u'n1 <- local_normal_at(t, point({x:g}, {y:g}, {z:g}))')
def step_calculate_local_normal_n1_of_t_at_point(context, x, y, z):
    context.n1 = context.t.local_normal_at(point(x, y, z))


@when(u'n2 <- local_normal_at(t, point({x:g}, {y:g}, {z:g}))')
def step_calculate_local_normal_n2_of_t_at_point(context, x, y, z):
    context.n2 = context.t.local_normal_at(point(x, y, z))


@when(u'n3 <- local_normal_at(t, point({x:g}, {y:g}, {z:g}))')
def step_calculate_local_normal_n3_of_t_at_point(context, x, y, z):
    context.n3 = context.t.local_normal_at(point(x, y, z))


@when(u'xs <- local_intersect(t, r)')
def step_set_xs_to_local_intersections_of_t_r(context):
    context.xs = context.t.local_intersect(context.r)


@then(u't.p1 = p1')
def step_assert_p1_of_triangle(context):
    assert_tuple(context.t.p1, context.p1)


@then(u't.p2 = p2')
def step_assert_p2_of_triangle(context):
    assert_tuple(context.t.p2, context.p2)


@then(u't.p3 = p3')
def step_assert_p3_of_triangle(context):
    assert_tuple(context.t.p3, context.p3)


@then(u't.e1 = vector(-1, -1, 0)')
def step_assert_e1_of_triangle(context):
    assert_tuple(context.t.e1, vector(-1, -1, 0))


@then(u't.e2 = vector(1, -1, 0)')
def step_assert_e2_of_triangle(context):
    assert_tuple(context.t.e2, vector(1, -1, 0))


@then(u't.normal = vector(0, 0, -1)')
def step_assert_normal_of_triangle(context):
    assert_tuple(context.t.normal, vector(0, 0, -1))


@then(u'{var_name} = t.normal')
def step_assert_var_equals_normal_of_triangle(context, var_name):
    var = getattr(context, var_name, None)
    assert_tuple(var, context.t.normal)
