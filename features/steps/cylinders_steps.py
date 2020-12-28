from behave import given, when, then  # pylint: disable=no-name-in-module
from shapes import Cylinder


@given(u'c <- cylinder()')
def step_create_cylinder_c(context):
    context.c = Cylinder()
