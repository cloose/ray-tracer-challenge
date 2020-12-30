from math import sqrt
from behave import given, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from core import vector
from shapes import Cone


@given(u'c <- cone()')
def step_create_cone_c(context):
    context.c = Cone()


@then(u'normal = vector(1, -sqrt(2), 1)')
def step_assert_normal_equals_vector(context):
    assert_tuple(context.normal, vector(1, -sqrt(2), 1))
