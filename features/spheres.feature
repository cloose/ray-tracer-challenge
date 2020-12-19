Feature: spheres

Scenario: A sphere is a shape
  Given s <- sphere()
  Then s is a shape

Scenario: A ray intersects a sphere at two points
  Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s <- sphere()
  When xs <- local_intersect(s, r)
  Then xs.count = 2
  And xs[0].t = 4.0
  And xs[1].t = 6.0

Scenario: A ray intersects a sphere at a tangent
  Given r <- ray(point(0, 1, -5), vector(0, 0, 1))
  And s <- sphere()
  When xs <- local_intersect(s, r)
  Then xs.count = 2
  And xs[0].t = 5.0
  And xs[1].t = 5.0

Scenario: A ray misses a sphere
  Given r <- ray(point(0, 2, -5), vector(0, 0, 1))
  And s <- sphere()
  When xs <- local_intersect(s, r)
  Then xs is empty

Scenario: A ray originates inside a sphere
  Given r <- ray(point(0, 0, 0), vector(0, 0, 1))
  And s <- sphere()
  When xs <- local_intersect(s, r)
  Then xs.count = 2
  And xs[0].t = -1.0
  And xs[1].t = 1.0

Scenario: A sphere is behind a ray
  Given r <- ray(point(0, 0, 5), vector(0, 0, 1))
  And s <- sphere()
  When xs <- local_intersect(s, r)
  Then xs.count = 2
  And xs[0].t = -6.0
  And xs[1].t = -4.0

Scenario: Intersect sets the object on the intersection
  Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s <- sphere()
  When xs <- local_intersect(s, r)
  Then xs.count = 2
  And xs[0].object = s
  And xs[1].object = s

Scenario: Intersecting a scaled sphere with a ray
  Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s <- sphere()
  And B <- scaling(2, 2, 2)
  When set_transform(s, B)
  And xs <- intersect(s, r)
  Then xs.count = 2
  And xs[0].t = 3
  And xs[1].t = 7

Scenario: Intersecting a translated sphere with a ray
  Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s <- sphere()
  And C <- translation(5, 0, 0)
  When set_transform(s, C)
  And xs <- intersect(s, r)
  Then xs is empty

Scenario: The normal on a sphere at a point on the x axis
  Given s <- sphere()
  When n <- local_normal_at(s, point(1, 0, 0))
  Then n = vector(1, 0, 0)

Scenario: The normal on a sphere at a point on the y axis
  Given s <- sphere()
  When n <- local_normal_at(s, point(0, 1, 0))
  Then n = vector(0, 1, 0)

Scenario: The normal on a sphere at a point on the z axis
  Given s <- sphere()
  When n <- local_normal_at(s, point(0, 0, 1))
  Then n = vector(0, 0, 1)

Scenario: The normal on a sphere at a nonaxial point
  Given s <- sphere()
  When n <- local_normal_at(s, point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
  Then n = vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3)

Scenario: A helper for producing a sphere with a glassy material
  Given s <- glass_sphere()
  Then s.transform = identity_matrix
  And s.material.transparency = 1.0
  And s.material.refractive_index = 1.5
