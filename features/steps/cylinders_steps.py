import math
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_float
from shapes import Cylinder


@given(u'c <- cylinder()')
def step_create_cylinder_c(context):
    context.c = Cylinder()


@given(u'c.minimum <- {expected:g}')
def step_set_minimum_of_cylinder_c(context, expected):
    context.c.minimum = expected


@given(u'c.maximum <- {expected:g}')
def step_set_maximum_of_cylinder_c(context, expected):
    context.c.maximum = expected


@given(u'c.closed <- {expected}')
def step_set_closed_of_cylinder_c(context, expected):
    context.c.closed = (expected.lower() == "true")


@then(u'c.maximum = {expected}')
def step_assert_maximum_of_cylinder_c(context, expected):
    if isinstance(expected, str) and expected == 'infinity':
        assert context.c.maximum == math.inf, \
                f"{context.c.maximum} is not infinity"


@then(u'c.minimum = {expected}')
def step_assert_minimum_of_cylinder_c(context, expected):
    if isinstance(expected, str) and expected == '-infinity':
        assert context.c.minimum == -math.inf, \
                f"{context.c.minimum} is not -infinity"


@then(u'c.closed = {expected}')
def step_assert_closed_of_cylinder_c(context, expected):
    assert context.c.closed == (expected.lower() == "true")
