from yaml import safe_load
from behave import given  # pylint: disable=no-name-in-module


@given(u'data <- yaml')
def step_load_yaml_into_data(context):
    context.data = safe_load(context.text)
