from math import sqrt
from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_float, assert_tuple
from core import point, vector
from shapes import Material, Sphere, Shape
from core import identity_matrix, multiply
from core import translation, scaling, rotation_z
from patterns_steps import TestPattern

TRANSFORMATIONS = {
    'scaling(2, 2, 2)': scaling(2, 2, 2),
    'translation(0, 0, 0.25)': translation(0, 0, 0.25),
    'translation(0, 0, -0.25)': translation(0, 0, -0.25),
    'translation(0, 0, 1)': translation(0, 0, 1),
}


def glass_sphere():
    sphere = Sphere()
    sphere.material.transparency = 1.0
    sphere.material.refractive_index = 1.5
    return sphere


def set_sphere_attributes(sphere, table):
    for row in table:
        if row['variable'] == 'material.ambient':
            sphere.material.ambient = float(row['value'])
            print(f'ambient={sphere.material.ambient}')

        if row['variable'] == 'material.transparency':
            sphere.material.transparency = float(row['value'])
            print(f'transparency={sphere.material.transparency}')

        if row['variable'] == 'material.refractive_index':
            sphere.material.refractive_index = float(row['value'])
            print(f'refractive_index={sphere.material.refractive_index}')

        if row['variable'] == 'material.pattern':
            sphere.material.pattern = TestPattern()
            print('pattern')

        if row['variable'] == 'transform':
            sphere.set_transform(TRANSFORMATIONS.get(row['value']))


@given(u's <- sphere()')
def step_create_sphere_s(context):
    context.s = Sphere()


@given(u's <- glass_sphere()')
def step_create_glass_sphere_s(context):
    context.s = glass_sphere()


@given(u's1 <- sphere()')
def step_create_sphere_s1(context):
    context.s1 = Sphere()


@given(u's2 <- sphere()')
def step_create_sphere_s2(context):
    context.s2 = Sphere()


@given(u's2 <- glass_sphere() with')
def step_create_glass_sphere_s2_with(context):
    context.s2 = glass_sphere()
    set_sphere_attributes(context.s2, context.table)


@given(u'A <- glass_sphere() with')
def step_create_glass_sphere_a_with(context):
    context.A = glass_sphere()
    set_sphere_attributes(context.A, context.table)


@given(u'B <- glass_sphere() with')
def step_create_glass_sphere_b_with(context):
    context.B = glass_sphere()
    set_sphere_attributes(context.B, context.table)


@given(u'C <- glass_sphere() with')
def step_create_glass_sphere_c_with(context):
    context.C = glass_sphere()
    set_sphere_attributes(context.C, context.table)


@given(u's1 has')
def step_set_attributes_of_sphere_s1(context):
    set_sphere_attributes(context.s1, context.table)


@given(u's2 has')
def step_set_attributes_of_sphere_s2(context):
    set_sphere_attributes(context.s2, context.table)


@when(u's <- Sphere.from_yaml(data)')
def step_create_sphere_s_from_yaml(context):
    context.s = Sphere.from_yaml(context.data)


@when(u'set_transform(s, B)')
def step_set_transform_of_s_to_b(context):
    context.s.set_transform(context.B)


@when(u'set_transform(s, C)')
def step_set_transform_of_s_to_c(context):
    context.s.set_transform(context.C)


@when(u'xs <- local_intersect(s, r)')
def step_assign_local_intersect_s_r_to_xs(context):
    context.xs = context.s.local_intersect(context.r)


@when(u'n <- local_normal_at(s, point({x:g}, {y:g}, {z:g}))')
def step_assign_local_normal_of_s_at_point_to_n(context, x, y, z):
    context.n = context.s.local_normal_at(point(x, y, z))


@when(u'n <- local_normal_at(s, point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))')
def step_assign_local_normal_of_s_at_certain_point_to_n(context):
    xyz = sqrt(3) / 3
    context.n = context.s.local_normal_at(point(xyz, xyz, xyz))


@then(u's is a shape')
def step_assert_s_is_a_shape(context):
    assert isinstance(context.s, Shape)


@then(u'xs is empty')
def step_assert_xs_is_empty(context):
    assert not context.xs


@then(u'xs.count = {expected:d}')
def step_assert_count_of_xs(context, expected):
    actual = len(context.xs)
    assert_float(actual, expected)


@then(u'xs[{index:d}].object = {shape}')
def step_assert_object_of_xs_at_index_equals_s(context, index, shape):
    actual = context.xs[index].object
    expected = getattr(context, shape, None)
    assert actual == expected, f"{actual} is not {expected} ({shape})"


@then(u'xs[{index:d}].t = {expected:g}')
def step_assert_t_of_xs_at_index(context, index, expected):
    actual = context.xs[index].t
    assert_float(actual, expected)


@then(u's.transform = C')
def step_assert_transform_of_s_equals_c(context):
    assert context.s.transform() == context.C


@then(u'n = vector({x:g}, {y:g}, {z:g})')
def step_assert_n_equals_vector(context, x, y, z):
    assert_tuple(context.n, vector(x, y, z))


@then(u'n = vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3)')
def step_assert_n_equals_certain_vector(context):
    xyz = sqrt(3) / 3
    assert_tuple(context.n, vector(xyz, xyz, xyz))


@then(u's.material.transparency = {expected:g}')
def step_assert_transparency_of_s_material(context, expected):
    assert_float(context.s.material.transparency, expected)


@then(u's.material.refractive_index = {expected:g}')
def step_assert_refractive_index_of_s_material(context, expected):
    assert_float(context.s.material.refractive_index, expected)
