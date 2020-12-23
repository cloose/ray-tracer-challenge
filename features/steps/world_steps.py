from behave import given, when, then  # pylint: disable=no-name-in-module
from asserts import assert_tuple, assert_float
from tuples import color
from transformations import scaling, translation
from shapes import Plane, Sphere
from world import World

TRANSFORMATIONS = {
    'scaling(0.5, 0.5, 0.5)': scaling(0.5, 0.5, 0.5),
    'translation(0, 0, 10)': translation(0, 0, 10),
    'translation(0, 0, 1)': translation(0, 0, 1),
    'translation(0, -1, 0)': translation(0, -1, 0),
    'translation(0, 1, 0)': translation(0, 1, 0),
    'translation(0, -3.5, -0.5)': translation(0, -3.5, -0.5)
}


def set_shape_attributes(shape, table):
    for row in table:
        if row['variable'] == 'material.color' and row['value'] == '(1, 0, 0)':
            shape.material.color = color(1, 0, 0)

        if row['variable'] == 'material.ambient':
            shape.material.ambient = float(row['value'])

        if row['variable'] == 'material.transparency':
            shape.material.transparency = float(row['value'])

        if row['variable'] == 'material.reflective':
            shape.material.reflective = float(row['value'])

        if row['variable'] == 'material.refractive_index':
            shape.material.refractive_index = float(row['value'])

        if row['variable'] == 'transform':
            shape.set_transform(TRANSFORMATIONS.get(row['value']))


@given(u'w <- world()')
def step_create_world_w(context):
    context.w = World()


@given(u'w <- default_world()')
def step_create_default_world_w(context):
    context.w = World.default()


@given(u's1 <- sphere() with')
def step_create_sphere_s1_with(context):
    context.s1 = Sphere()
    context.s1.material.color = color(0.8, 1.0, 0.6)
    context.s1.material.diffuse = 0.7
    context.s1.material.specular = 0.2


@given(u's2 <- sphere() with')
def step_create_sphere_s2_with(context):
    context.s2 = Sphere()
    set_shape_attributes(context.s2, context.table)


@given(u'p <- plane() with')
def step_create_plane_p_with(context):
    context.p = Plane()
    set_shape_attributes(context.p, context.table)


@given(u'p2 <- plane() with')
def step_create_plane_p2_with(context):
    context.p2 = Plane()
    for row in context.table:
        if row['variable'] == 'material.reflective':
            context.p2.material.reflective = float(row['value'])

        if row['variable'] == 'transform':
            context.p2.set_transform(TRANSFORMATIONS.get(row['value']))


@given(u's1 <- the first object in w')
def step_set_s1_to_first_object_w(context):
    context.s1 = context.w.objects[0]


@given(u's2 <- the second object in w')
def step_set_s2_to_second_object_w(context):
    context.s2 = context.w.objects[1]


@given(u's1.material.ambient <- 1')
def step_assign_s1_material_ambient(context):
    context.s1.material.ambient = 1


@given(u's2.material.ambient <- 1')
def step_assign_s2_material_ambient(context):
    context.s2.material.ambient = 1


@given(u's is added to w')
def step_add_s_to_w(context):
    context.w.objects.append(context.s)


@given(u's2 is added to w')
def step_add_s2_to_w(context):
    context.w.objects.append(context.s2)


@given(u'p is added to w')
def step_add_p_to_w(context):
    context.w.objects.append(context.p)


@given(u'p2 is added to w')
def step_add_p2_to_w(context):
    context.w.objects.append(context.p2)


@when(u'w.light <- light')
def step_set_light_of_w_to_light(context):
    context.w.light = context.light


@when(u'c <- shade_hit(w, shape_hit)')
def step_set_c_to_shade_hit_w_shape_hit(context):
    context.c = context.w.shade_hit(context.shape_hit)


@when(u'c <- shade_hit(w, shape_hit, {remaining:d})')
def step_set_c_to_shade_hit_w_shape_hit_with_remaining(context, remaining):
    context.c = context.w.shade_hit(context.shape_hit, remaining)


@when(u'xs <- intersect_world(w, r)')
def step_set_xs_to_intersect_world_w_r(context):
    context.xs = context.w.intersect(context.r)


@when(u'c <- color_at(w, r)')
def step_set_s_to_color_at_w_r(context):
    context.c = context.w.color_at(context.r)


@when(u'c <- reflected_color(w, shape_hit)')
def step_set_c_to_reflected_color_w_shape_hit(context):
    context.c = context.w.reflected_color(context.shape_hit)


@when(u'c <- reflected_color(w, shape_hit, {remaining:d})')
def step_set_c_to_reflected_color_w_shape_hit(context, remaining):
    context.c = context.w.reflected_color(context.shape_hit, remaining)


@when(u'c <- refracted_color(w, shape_hit, {remaining:d})')
def step_impl(context, remaining):
    context.c = context.w.refracted_color(context.shape_hit, remaining)


@then(u'w contains no objects')
def step_assert_w_has_no_objects(context):
    assert not context.w.objects


@then(u'w has no light source')
def step_assert_w_has_no_light(context):
    assert not context.w.light


@then(u'w.light = light')
def step_assert_w_has_light(context):
    assert_tuple(context.w.light.position, context.light.position)
    assert_tuple(context.w.light.intensity, context.light.intensity)


@then(u'w contains s1')
def step_assert_w_contains_s1(context):
    actual = context.w.objects[0]
    assert_tuple(actual.material.color, context.s1.material.color)
    assert_float(actual.material.diffuse, context.s1.material.diffuse)
    assert_float(actual.material.specular, context.s1.material.specular)


@then(u'w contains s2')
def step_assert_w_contains_s2(context):
    actual = context.w.objects[1]
    assert actual.transform() == scaling(0.5, 0.5, 0.5)


@then(u'c = s2.material.color')
def step_assert_c_equals_s2_material_color(context):
    assert_tuple(context.c, context.s2.material.color)


@then(u'is_shadowed(w, p) is {expected}')
def step_assert_p_is_not_in_shaddow(context, expected):
    assert context.w.is_shadowed(context.p) == (expected.lower() == "true")


@then(u'color_at(w, r) should terminate successfully')
def step_assert_color_at_terminates(context):
    assert not context.w.color_at(context.r) is None
