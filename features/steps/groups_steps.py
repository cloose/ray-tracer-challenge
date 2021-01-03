from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_matrix
from core import identity_matrix, scaling
from shapes import Group


@given(u'g <- group()')
def step_create_group_g(context):
    context.g = Group()


@given(u'g1 <- group()')
def step_create_group_g1(context):
    context.g1 = Group()


@given(u'g2 <- group()')
def step_create_group_g2(context):
    context.g2 = Group()


@when(u'add_child({group_var}, {shape_var})')
def step_add_child_shape_s_to_group_g(context, group_var, shape_var):
    group = getattr(context, group_var, None)
    shape = getattr(context, shape_var, None)
    group.add_child(shape)


@when(u'xs <- intersect(g, r)')
def step_assign_intersect_of_group_and_ray_to_xs(context):
    context.xs = context.g.intersect(context.r)


@when(u'xs <- local_intersect(g, r)')
def step_assign_local_intersect_of_group_and_ray_to_xs(context):
    context.xs = context.g.local_intersect(context.r)


@then(u'g.transform = identity_matrix')
def step_assert_transform_of_g_equals_identity_matrix(context):
    assert_matrix(context.g.transform(), identity_matrix())


@then(u'g is empty')
def step_assert_group_g_is_empty(context):
    assert not context.g.children, \
            f"children is not empty: {context.g.children}"


@then(u'g is not empty')
def step_assert_group_g_is_not_empty(context):
    assert context.g.children, \
            f"children is empty: {context.g.children}"
