from math import sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from intersection import Intersection, hit


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


@given(u'xs <- intersections(i1)')
def step_create_intersections_xs_with_i1(context):
    context.xs = [context.i1]


@given(u'xs <- intersections(i2, i1)')
def step_impl(context):
    context.xs = [context.i2, context.i1]


@given(u'xs <- intersections(i1, i2, i3, i4)')
def step_impl(context):
    context.xs = [context.i1, context.i2, context.i3, context.i4]


@given(u'xs <- intersections(2:A, 2.75:B, 3.25:C, 4.75:B, 5.25:C, 6:A)')
def step_create_intersections_xs_from_a_b_c(context):
    context.xs = [
        Intersection(2, context.A),
        Intersection(2.75, context.B),
        Intersection(3.25, context.C),
        Intersection(4.75, context.B),
        Intersection(5.25, context.C),
        Intersection(6.0, context.A)
    ]


@given(u'xs <- intersections(4:s1, 6:s1)')
def step_impl(context):
    context.xs = [Intersection(4, context.s1), Intersection(6, context.s1)]


@given(u'xs <- intersections(-sqrt(2)/2:s1, sqrt(2)/2:s1)')
def step_impl(context):
    context.xs = [
        Intersection(-sqrt(2) / 2, context.s1),
        Intersection(sqrt(2) / 2, context.s1)
    ]


@given(u'xs <- intersections(-0.9899:s1, -0.4899:s2, 0.4899:s2, 0.9899:s1)')
def step_impl(context):
    context.xs = [
        Intersection(-0.9899, context.s1),
        Intersection(-0.4899, context.s2),
        Intersection(0.4899, context.s2),
        Intersection(0.9899, context.s1)
    ]


@given(u'xs <- intersections(sqrt(2):p)')
def step_impl(context):
    context.xs = [Intersection(sqrt(2), context.p)]


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
