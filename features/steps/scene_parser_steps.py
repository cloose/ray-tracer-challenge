from behave import when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple, assert_matrix
from core import color
from core import multiply_matrix
from core import translation, scaling
from scene import scene_from_yaml


@when(u'w <- scene_from_yaml(data)')
def step_parse_scene_from_yaml_into_world_w(context):
    _, context.w = scene_from_yaml(context.data)


@when(u'c <- scene_from_yaml(data)')
def step_parse_scne_from_yaml_into_camera_c(context):
    context.c, _ = scene_from_yaml(context.data)


@then(u'w.objects.count = {expected:d}')
def step_assert_world_objects_count(context, expected):
    actual = len(context.w.objects)
    assert actual == expected, \
            f"count: {actual} is not equal to {expected}"


@then(
    u'w.objects[{index:d}].material.color = color({red:g}, {green:g},{blue:g})'
)
def step_assert_material_color_of_object_at_index(context, index, red, green,
                                                  blue):
    assert_tuple(context.w.objects[index].material.color,
                 color(red, green, blue))


@then(u'w.objects[{index:d}].material.ambient = {expected:g}')
def step_impl(context, index, expected):
    assert_float(context.w.objects[index].material.ambient, expected)


@then(
    u'w.objects[{index:d}].transform = scaling({sx:g}, {sy:g}, {sz:g}) * translation({tx:g}, {ty:g}, {tz:g})'
)
def step_assert_transformation_matrix_of_object_at_index(
    context, index, tx, ty, tz, sx, sy, sz):
    assert_matrix(
        context.w.objects[index].transform(),
        multiply_matrix(scaling(sx, sy, sz), translation(tx, ty, tz)))
