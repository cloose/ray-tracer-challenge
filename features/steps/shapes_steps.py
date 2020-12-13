from math import pi, sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple
from tuples import point, vector, normalize
from matrix import identity_matrix, multiply
from transformations import translation, scaling, rotation_z
from material import Material
from shape import Shape


class TestShape(Shape):
    def __init__(self):
        self.saved_ray = None
        Shape.__init__(self)

    def local_intersect(self, local_ray):
        self.saved_ray = local_ray

    def local_normal_at(self, local_point):
        return vector(local_point[0], local_point[1], local_point[2])


@given(u's <- test_shape()')
def step_create_test_shape_s(context):
    context.s = TestShape()


@given(u'm <- scaling(1, 0.5, 1) * rotation_z(pi/5)')
def step_create_scaling_rotation_z_matrix_m(context):
    context.m = multiply(scaling(1, 0.5, 1), rotation_z(pi / 5))


@when(u'set_transform(s, m)')
def step_set_transform_of_s_to_m(context):
    context.s.set_transform(context.m)


@when(u'set_transform(s, translation({x:g}, {y:g}, {z:g}))')
def step_set_transform_of_s_to_translation_matrix(context, x, y, z):
    context.s.set_transform(translation(x, y, z))


@when(u'set_transform(s, scaling({x:g}, {y:g}, {z:g}))')
def step_set_transform_of_s_to_scaling_matrix(context, x, y, z):
    context.s.set_transform(scaling(x, y, z))


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


@then(u's.transform = identity_matrix')
def step_assert_transform_of_s_equals_identity_matrix(context):
    assert context.s.transform() == identity_matrix()


@then(u's.transform = translation(2, 3, 4)')
def step_assert_transform_of_s_equals_translation(context):
    assert context.s.transform() == translation(2, 3, 4)


@then(u's.material = material()')
def step_assert_material_of_s_equals_default_material(context):
    assert context.s.material == Material()


@then(u's.material = m')
def step_assert_material_of_s_equals_m(context):
    assert context.s.material == context.m


@then(u's.saved_ray.origin = point({x:g}, {y:g}, {z:g})')
def step_assert_saved_ray_origin_equals_point(context, x, y, z):
    assert_tuple(context.s.saved_ray.origin, point(x, y, z))


@then(u's.saved_ray.direction = vector({x:g}, {y:g}, {z:g})')
def step_assert_saved_ray_direction_equals_vector(context, x, y, z):
    assert_tuple(context.s.saved_ray.direction, vector(x, y, z))


@then(u'n = normalize(n)')
def step_assert_n_equals_normalized_n(context):
    assert_tuple(context.n, normalize(context.n))
