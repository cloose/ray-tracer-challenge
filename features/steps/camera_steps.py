from math import pi, sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple, assert_matrix
from core import color, identity_matrix, multiply_matrix, rotation_y, translation, view_transform
from scene import Camera
from ray_tracer import RayTracer


@given(u'c <- camera({hsize:d}, {vsize:d}, pi/2)')
def step_create_camera_c(context, hsize, vsize):
    context.c = Camera(hsize, vsize, pi / 2)


@when(u'c <- Camera.from_yaml(data)')
def step_create_camera_c_from_yaml(context):
    context.c = Camera.from_yaml(context.data)


@when(u'r2 <- ray_for_pixel(c, {x:d}, {y:d})')
def step_set_r_to_ray_for_pixel(context, x, y):
    context.r2 = context.c.ray_for_pixel(x, y)


@when(u'c.transform <- rotation_y(pi/4) * translation(0, -2, 5)')
def step_set_transform_of_c_to_transformation_matrix(context):
    context.c.set_transform(
        multiply_matrix(rotation_y(pi / 4), translation(0, -2, 5)))


@when(u'c.transform <- A')
def step_set_transform_of_c_to_a(context):
    context.c.set_transform(context.a)


@when(u'image <- render(c, w)')
def step_set_image_to_render_c_w(context):
    context.image = RayTracer().render(context.c, context.w)


@then(u'c.hsize = {hsize:d}')
def step_assert_hsize_of_c(context, hsize):
    assert_float(context.c.horizontal_size_px, hsize)


@then(u'c.vsize = {vsize:d}')
def step_assert_vsize_of_c(context, vsize):
    assert_float(context.c.vertical_size_px, vsize)


@then(u'c.field_of_view = pi/2')
def step_assert_field_of_view_of_c(context):
    assert_float(context.c.field_of_view, pi / 2)


@then(u'c.transform = identity_matrix')
def step_assert_transform_of_c_equals_identity_matrix(context):
    assert context.c.transform() == identity_matrix()


@then(u'c.transform = view_transform(p, to, up)')
def step_assert_transform_of_c_equals_view_transform(context):
    assert_matrix(context.c.transform(),
                  view_transform(context.p, context.to, context.up))


@then(u'c.pixel_size = {expected:g}')
def step_assert_pixel_size_of_c(context, expected):
    assert_float(context.c.pixel_size, expected)


@then(u'pixel_at(image, {x:d}, {y:d}) = color({red:g}, {green:g}, {blue:g})')
def step_pixel_at_coordinates_equals_color(context, x, y, red, green, blue):
    assert_tuple(context.image.pixel_at(x, y), color(red, green, blue))
