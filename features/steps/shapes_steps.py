from math import pi, sqrt

from behave import given, then, when  # pylint: disable=no-name-in-module

from asserts import assert_matrix, assert_tuple
from core import (color, identity_matrix, multiply_matrix, normalize, point,
                  rotation_y, rotation_z, scaling, translation, vector)
from shapes import Material, Shape


class TestShape(Shape):
    def __init__(self):
        self.saved_ray = None
        Shape.__init__(self)

    def local_intersect(self, local_ray):
        self.saved_ray = local_ray

    def local_normal_at(self, local_point, hit=None):
        return vector(local_point[0], local_point[1], local_point[2])


@given(u's <- test_shape()')
def step_create_test_shape_s(context):
    context.s = TestShape()


@given(u'A <- test_shape()')
def step_create_test_shape_a(context):
    context.A = TestShape()


@given(u'B <- test_shape()')
def step_create_test_shape_b(context):
    context.B = TestShape()


@given(u'm <- scaling(1, 0.5, 1) * rotation_z(pi/5)')
def step_create_scaling_rotation_z_matrix_m(context):
    context.m = multiply_matrix(scaling(1, 0.5, 1), rotation_z(pi / 5))


@when(u'set_transform(s, m)')
def step_set_transform_of_s_to_m(context):
    context.s.set_transform(context.m)


@when(u'set_transform({shape_var}, translation({x:g}, {y:g}, {z:g}))')
def step_set_transform_of_shape_to_translation_matrix(context, shape_var, x, y,
                                                      z):
    shape = getattr(context, shape_var, None)
    shape.set_transform(translation(x, y, z))


@when(u'set_transform({shape_var}, scaling({x:g}, {y:g}, {z:g}))')
def step_set_transform_of_shape_to_scaling_matrix(context, shape_var, x, y, z):
    shape = getattr(context, shape_var, None)
    shape.set_transform(scaling(x, y, z))


@when(u'set_transform({shape_var}, rotation_y({value}))')
def step_set_transform_of_shape_to_rotation_y_matrix(context, shape_var,
                                                     value):
    shape = getattr(context, shape_var, None)

    if value == 'pi/2':
        angle = pi / 2
    else:
        angle = float(value)

    shape.set_transform(rotation_y(angle))


@when(u's.material <- m')
def step_set_material_of_s_to_m(context):
    context.s.material = context.m


@when(u'xs <- intersect(s, r)')
def step_assign_intersect_s_r_to_xs(context):
    context.xs = context.s.intersect(context.r)


@when(u'n <- normal_at(s, point({x:g}, {y:g}, {z:g}))')
def step_assign_normal_of_s_at_point_to_n(context, x, y, z):
    context.n = context.s.normal_at(point(x, y, z))


@when(u'n <- normal_at(s, point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))')
def step_assign_normal_of_s_at_certain_point_to_n(context):
    xyz = sqrt(3) / 3
    context.n = context.s.normal_at(point(xyz, xyz, xyz))


@when(u'n <- normal_at(s, point(0, sqrt(2)/2, -sqrt(2)/2))')
def step_assign_normal_of_s_at_another_point_to_n(context):
    xyz = sqrt(2) / 2
    context.n = context.s.normal_at(point(0, xyz, -xyz))


@when(u'p <- world_to_object(s, point({x:g}, {y:g}, {z:g}))')
def step_assign_world_to_object_of_point_to_p(context, x, y, z):
    context.p = context.s.world_to_object(point(x, y, z))


@when(u'n <- normal_to_world(s, vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))')
def step_assign_normal_to_world_of_vector_to_p(context):
    xyz = sqrt(3) / 3
    context.n = context.s.normal_to_world(vector(xyz, xyz, xyz))


@then(u's.parent is nothing')
def step_assert_parent_of_s_is_nothing(context):
    assert context.s.parent is None, \
            f"{context.s.parent} is not None"


@then(u'{shape_name}.parent = {parent_name}')
def step_assert_parent_of_s_equals_g(context, shape_name, parent_name):
    shape = getattr(context, shape_name)
    parent = getattr(context, parent_name)
    assert shape.parent == parent, \
            f"{shape.parent} is not {parent}"


@then(u'{shape_a:w} includes {shape_b:w}')
def step_assert_shape_includes(context, shape_a, shape_b):
    a = getattr(context, shape_a)
    b = getattr(context, shape_b)
    assert a.includes(b)


@then(u'{shape_a:w} not includes {shape_b:w}')
def step_assert_shape_not_includes(context, shape_a, shape_b):
    a = getattr(context, shape_a)
    b = getattr(context, shape_b)
    assert not a.includes(b)


@then(u's.cast_shadow = {expected}')
def step_assert_cast_shadow_of_s(context, expected):
    assert context.s.cast_shadow == (expected.lower() == "true")


@then(u's.transform = identity_matrix')
def step_assert_transform_of_s_equals_identity_matrix(context):
    assert_matrix(context.s.transform(), identity_matrix())


@then(u's.transform = translation({x:g}, {y:g}, {z:g})')
def step_assert_transform_of_s_equals_translation(context, x, y, z):
    assert_matrix(context.s.transform(), translation(x, y, z))


@then(u's.material = material()')
def step_assert_material_of_s_equals_default_material(context):
    assert context.s.material == Material()


@then(u's.material = m')
def step_assert_material_of_s_equals_m(context):
    assert context.s.material == context.m


@then(u's.material.color = color({red:g}, {green:g}, {blue:g})')
def step_assert_material_color_of_s_equals_color(context, red, green, blue):
    assert_tuple(context.s.material.color, color(red, green, blue))


@then(u's.saved_ray.origin = point({x:g}, {y:g}, {z:g})')
def step_assert_saved_ray_origin_equals_point(context, x, y, z):
    assert_tuple(context.s.saved_ray.origin, point(x, y, z))


@then(u's.saved_ray.direction = vector({x:g}, {y:g}, {z:g})')
def step_assert_saved_ray_direction_equals_vector(context, x, y, z):
    assert_tuple(context.s.saved_ray.direction, vector(x, y, z))


@then(u'n = normalize(n)')
def step_assert_n_equals_normalized_n(context):
    assert_tuple(context.n, normalize(context.n))


@then(u'p = point({x:g}, {y:g}, {z:g})')
def step_assert_p_equals_point(context, x, y, z):
    assert_tuple(context.p, point(x, y, z))
