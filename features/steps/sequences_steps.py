from itertools import cycle

from behave import given, then, when  # pylint: disable=no-name-in-module

from asserts import assert_float


@given(u'gen <- sequence({values})')
def step_create_sequence_gen(context, values):
    value_list = [float(x.strip()) for x in values.split(',')]
    context.gen = cycle(value_list)


@then(u'next(gen) = {expected:g}')
def step_assert_next_value_of_sequence_gen(context, expected):
    assert_float(next(context.gen), expected)
