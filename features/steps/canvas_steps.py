from canvas import Canvas
from tuples import color

@given(u'c <- canvas({w:d}, {h:d})')
def step_impl(context, w, h):
    context.c = Canvas(w, h)


@given(u'red <- color(1, 0, 0)')
def step_impl(context):
    context.red = color(1, 0, 0)


@when(u'every pixel of c is set to color({r:g}, {g:g}, {b:g})')
def step_impl(context, r, g, b):
    for y in range(context.c.height):
        for x in range(context.c.width):
            context.c.set_pixel(x, y, color(r, g, b))


@when(u'write_pixel(c, 2, 3, red)')
def step_impl(context):
    context.c.set_pixel(2, 3, context.red)


@when(u'write_pixel(c, 0, 0, c1)')
def step_impl(context):
    context.c.set_pixel(0, 0, context.c1)


@when(u'write_pixel(c, 2, 1, c2)')
def step_impl(context):
    context.c.set_pixel(2, 1, context.c2)


@when(u'write_pixel(c, 4, 2, c3)')
def step_impl(context):
    context.c.set_pixel(4, 2, context.c3)


@when(u'ppm <- canvas_to_ppm(c)')
def step_impl(context):
    context.ppm = context.c.to_ppm()


@then(u'c.width = 10')
def step_impl(context):
    assert context.c.width == 10


@then(u'c.height = 20')
def step_impl(context):
    assert context.c.height == 20


@then(u'every pixel of c is color(0, 0, 0)')
def step_impl(context):
    for px in context.c.pixels:
        assert px == color(0, 0, 0)


@then(u'pixel_at(c, 2, 3) = red')
def step_impl(context):
    assert context.c.pixel_at(2, 3) == context.red


@then(u'lines {s:d}-{e:d} of ppm are')
def step_impl(context, s, e):
    text = context.text.splitlines()
    ppm = context.ppm.splitlines()[s-1:e]
    assert ppm == text, "%r is not %r" % (ppm, text)


@then(u'the last character of ppm is a newline')
def step_impl(context):
    assert context.ppm[-1] == '\n'
