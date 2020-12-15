from math import sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from intersection import Intersection, hit

_EPSILON = 0.00001


@given(u'i1 <- intersection({t:g}, s)')
def step_impl(context, t):
    context.i1 = Intersection(t, context.s)


@given(u'i1 <- intersection(sqrt(2), p)')
def step_determine_intersection_i1_at_sqrt_2_for_p(context):
    context.i1 = Intersection(sqrt(2), context.p)


@given(u'i1 <- intersection({t:g}, s1)')
def step_impl(context, t):
    context.i1 = Intersection(t, context.s1)


@given(u'i1 <- intersection({t:g}, s2)')
def step_impl(context, t):
    context.i1 = Intersection(t, context.s2)


@given(u'i2 <- intersection({t:g}, s)')
def step_impl(context, t):
    context.i2 = Intersection(t, context.s)


@given(u'i3 <- intersection({t:g}, s)')
def step_impl(context, t):
    context.i3 = Intersection(t, context.s)


@given(u'i4 <- intersection({t:g}, s)')
def step_impl(context, t):
    context.i4 = Intersection(t, context.s)


@given(u'xs <- intersections(i2, i1)')
def step_impl(context):
    context.xs = [context.i2, context.i1]


@given(u'xs <- intersections(i1, i2, i3, i4)')
def step_impl(context):
    context.xs = [context.i1, context.i2, context.i3, context.i4]


@when(u'i <- intersection({t:g}, s)')
def step_impl(context, t):
    context.i = Intersection(t, context.s)


@when(u'xs <- intersections(i1, i2)')
def step_impl(context):
    context.xs = [context.i1, context.i2]


@when(u'i <- hit(xs)')
def step_impl(context):
    context.i = hit(context.xs)


@then(u'i.t = {expected:g}')
def step_impl(context, expected):
    assert context.i.t == expected, f"{context.i.t} is not {expected}"


@then(u'i.object = s')
def step_impl(context):
    assert context.i.object == context.s, f"{context.i.object} is not {context.s}"


@then(u'i is nothing')
def step_impl(context):
    assert context.i == None, f"{context.i} is not None"


@then(u'i = i1')
def step_impl(context):
    assert context.i == context.i1, f"{context.i} is not {context.i1}"


@then(u'i = i2')
def step_impl(context):
    assert context.i == context.i2, f"{context.i} is not {context.i2}"


@then(u'i = i4')
def step_impl(context):
    assert context.i == context.i4, f"{context.i} is not {context.i4}"


@then(u'shape_hit.over_point.z < -EPSILON/2')
def step_assert_over_point_z_less_than_negative_half_epsilon(context):
    assert context.shape_hit.over_point[2] < -(_EPSILON / 2), \
            f"{context.shape_hit.over_point[2]} is not less than {-(_EPSILON/2)}"


@then(u'shape_hit.point.z > shape_hit.over_point.z')
def step_assert_point_z_greater_than_over_point_z(context):
    assert context.shape_hit.point[2] > context.shape_hit.over_point[2]
