from math import sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from core import Intersection, hit

INTERSECTION_BY_NAME = {
    'i1': lambda context: context.i1,
    'i2': lambda context: context.i2,
    'i3': lambda context: context.i3,
    'i4': lambda context: context.i4,
}

OBJECT_BY_NAME = {
    's': lambda context: context.s,
    's1': lambda context: context.s1,
    's2': lambda context: context.s2,
    'p': lambda context: context.p,
    'A': lambda context: context.A,
    'B': lambda context: context.B,
    'C': lambda context: context.C,
}


def create_intersections_from_string(context, intersections):
    result = []

    for part in intersections.split(','):
        part = part.strip()
        if ':' in part:
            (pos, obj) = part.split(':')
            if pos == 'sqrt(2)/2':
                pos_num = sqrt(2) / 2
            elif pos == '-sqrt(2)/2':
                pos_num = -sqrt(2) / 2
            elif pos == 'sqrt(2)':
                pos_num = sqrt(2)
            else:
                pos_num = float(pos)
            result.append(
                Intersection(pos_num,
                             OBJECT_BY_NAME.get(obj)(context)))
        else:
            print(part)
            result.append(INTERSECTION_BY_NAME.get(part)(context))

    return result


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


@given(u'xs <- intersections({intersection_list})')
def step_create_intersections_xs_from_list(context, intersection_list):
    intersections = create_intersections_from_string(context,
                                                     intersection_list)
    context.xs = intersections


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
