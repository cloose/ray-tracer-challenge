from tuples import tuple
from matrix import *

a = identity_matrix()
print(inverse(a))

a = identity_matrix()
a[1][0] = 2
a[0][3] = -5

b = multiply(a, inverse(a))
print(b)

c = inverse(transpose(a))
d = transpose(inverse(a))

print(c)
print(d)

t = tuple(5, 4, 3, 1)
i = identity_matrix()

c = multiply_tuple(i, t)
print(c)

i[1][1] = 2
i[2][2] = 3
c = multiply_tuple(i, t)
print(c)
