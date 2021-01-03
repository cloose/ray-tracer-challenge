from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from core import point, vector
from scene import parse_obj_file


@given(u'file <- a file containing')
def step_setup_file_containing_data(context):
    context.file = context.text.splitlines()


@when(u'parser <- parse_obj_file(file)')
def step_parse_obj_file(context):
    context.parser = parse_obj_file(context.file)


@when(u'g <- parser.default_group')
def step_assign_default_group_to_g(context):
    context.g = context.parser.groups["default"]


@when(u't1 <- first child of {group_name}')
def step_assign_first_child_of_group_to_t1(context, group_name):
    group = getattr(context, group_name, None)
    context.t1 = group.children[0]


@when(u't2 <- first child of {group_name}')
def step_assign_first_child_of_group_to_t2(context, group_name):
    group = getattr(context, group_name, None)
    context.t2 = group.children[0]


@when(u't2 <- second child of g')
def step_assign_second_child_of_g_to_t2(context):
    context.t2 = context.g.children[1]


@when(u't3 <- third child of g')
def step_assign_third_child_of_g_to_t3(context):
    context.t3 = context.g.children[2]


@when(u'g1 <- "FirstGroup" from parser')
def step_assign_firstgroup_to_g1(context):
    context.g1 = context.parser.groups["FirstGroup"]


@when(u'g2 <- "SecondGroup" from parser')
def step_assign_secondgroup_to_g2(context):
    context.g2 = context.parser.groups["SecondGroup"]


@when(u'g <- obj_to_group(parser)')
def step_assign_object_group_to_g(context):
    context.g = context.parser.obj_group()


@then(u'parser should have ignored 5 lines')
def step_assert_ignored_lines(context):
    assert context.parser.ignored == 5


@then(u'parser.vertices[{index:d}] = point({x:g}, {y:g}, {z:g})')
def step_assert_vertex_at_index(context, index, x, y, z):
    assert_tuple(context.parser.vertices[index], point(x, y, z))


@then(u'parser.normals[{index:d}] = vector({x:g}, {y:g}, {z:g})')
def step_assert_normal_at_index(context, index, x, y, z):
    assert_tuple(context.parser.normals[index], vector(x, y, z))


@then(u'{triangle_name}.{point_name} = parser.vertices[{index:d}]')
def step_assert_point_of_triangle_equals_vertex(context, triangle_name,
                                                point_name, index):
    triangle = getattr(context, triangle_name, None)
    p = getattr(triangle, point_name, None)
    assert_tuple(p, context.parser.vertices[index])


@then(u'{triangle_name}.{normal_name} = parser.normals[{index:d}]')
def step_assert_normal_of_triangle_equals_vector(context, triangle_name,
                                                 normal_name, index):
    triangle = getattr(context, triangle_name, None)
    n = getattr(triangle, normal_name, None)
    assert_tuple(n, context.parser.normals[index])


@then(u'g includes "{group_name}" from parser')
def step_assert_g_includes_group_of_name(context, group_name):
    expected = context.parser.groups[group_name]
    assert expected in context.g.children, \
            f"{context.g.children} does not include {expected}"


@then(u't2 = t1')
def step_assert_triangles_t2_t1_are_equal(context):
    assert_tuple(context.t2.p1, context.t1.p1)
    assert_tuple(context.t2.p2, context.t1.p2)
    assert_tuple(context.t2.p3, context.t1.p3)
    assert_tuple(context.t2.n1, context.t1.n1)
    assert_tuple(context.t2.n2, context.t1.n2)
    assert_tuple(context.t2.n3, context.t1.n3)
