from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_count
from shapes import CsgShape, intersection_allowed


@given(u'csg <- csg("{operation}", {left_name}, {right_name})')
def step_create_csg_from_shapes(context, operation, left_name, right_name):
    left = getattr(context, left_name)
    right = getattr(context, right_name)
    context.csg = CsgShape(operation, left, right)


@when(u'result <- intersection_allowed("{operation}", {lhit}, {inl}, {inr})')
def step_assign_intersection_allowed_to_result(context, operation, lhit, inl,
                                               inr):
    context.result = intersection_allowed(operation,
                                          lhit.lower() == "true",
                                          inl.lower() == "true",
                                          inr.lower() == "true")


@when(u'result <- filter_intersections(csg, xs)')
def step_assign_filter_intersections_to_result(context):
    context.result = context.csg.filter_intersections(context.xs)


@when(u'xs <- local_intersect(csg, r)')
def step_assign_local_intersect_to_xs(context):
    context.xs = context.csg.local_intersect(context.r)


@then(u'csg.operation = "{operation}"')
def step_assert_operation_of_csg(context, operation):
    assert context.csg.operation == operation, \
            f"{context.csg.operation} is not equal to {operation}"


@then(u'csg.left = {shape_name}')
def step_assert_left_shape_of_csg(context, shape_name):
    expected = getattr(context, shape_name)
    assert context.csg.left == expected, \
            f"{context.csg.left} is not {expected}"


@then(u'csg.right = {shape_name}')
def step_assert_right_shape_of_csg(context, shape_name):
    expected = getattr(context, shape_name)
    assert context.csg.right == expected, \
            f"{context.csg.right} is not {expected}"


@then(u'result = {expected}')
def step_assert_result(context, expected):
    assert context.result == (expected.lower() == "true"), \
            f"{context.result} is not equal to {expected}"


@then(u'result.count = {expected:d}')
def step_assert_count_of_result(context, expected):
    assert_count(context.result, expected)


@then(u'result[{index1:d}] = xs[{index2:d}]')
def step_assert_intersection_at_index(context, index1, index2):
    assert context.result[index1] == context.xs[index2], \
            f"{context.result[index1]} is not {context.xs[index2]}"
