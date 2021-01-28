from math import sqrt

from behave import given, then, when  # pylint: disable=no-name-in-module

from asserts import assert_tuple
from core import vector
from shapes import Cone


@given(u'c <- cone()')
def step_create_cone_c(context):
    context.c = Cone()


@when(u'c <- Cone.from_yaml(data)')
def step_create_cone_c_from_yaml(context):
    context.c = Cone.from_yaml(context.data)


@then(u'c.cast_shadow = {expected}')
def step_assert_cast_shadow_of_c(context, expected):
    assert context.c.cast_shadow == (expected.lower() == "true")


@then(u'normal = vector(1, -sqrt(2), 1)')
def step_assert_normal_equals_vector(context):
    assert_tuple(context.normal, vector(1, -sqrt(2), 1))
