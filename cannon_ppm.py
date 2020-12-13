from tuples import point, vector, color, add, normalize, multiply
from canvas import Canvas

def tick(env, proj):
   position = add(proj['position'], proj['velocity'])
   velocity = add(add(proj['velocity'], env['gravity']), env['wind'])
   return dict(position=position, velocity=velocity)

p = dict(position=point(0, 1, 0), velocity=multiply(normalize(vector(1, 1.8, 0)), 11.25))
e = dict(gravity=vector(0, -0.1, 0), wind=vector(-0.01, 0, 0))
c = Canvas(900, 550)

while p['position'][1] > 0.0:
    print('position %r, %r, %r' % (p['position'][0], p['position'][1], p['position'][2]))
    c.set_pixel(round(p['position'][0]), c.height - round(p['position'][1]), color(0.0, 1.0, 0.0))
    p = tick(e, p)

ppm = c.to_ppm()
f = open('cannon.ppm', 'w')
f.write(ppm)
