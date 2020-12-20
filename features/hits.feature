Feature: hits

Scenario: Precomputing the state of an Intersection
  Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s <- sphere()
  And i1 <- intersection(4, s)
  When shape_hit <- hit(i1, r)
  Then shape_hit.t = i1.t
  And shape_hit.object = i1.object
  And shape_hit.point = point(0, 0, -1)
  And shape_hit.eyev = vector(0, 0, -1)
  And shape_hit.normalv = vector(0, 0, -1)

Scenario: The hit, when an intersection occurs on the outside
  Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s <- sphere()
  And i1 <- intersection(4, s)
  When shape_hit <- hit(i1, r)
  Then shape_hit.inside = false

Scenario: The hit, when an intersection occurs on the inside
  Given r <- ray(point(0, 0, 0), vector(0, 0, 1))
  And s <- sphere()
  And i1 <- intersection(1, s)
  When shape_hit <- hit(i1, r)
  Then shape_hit.point = point(0, 0, 1)
  And shape_hit.eyev = vector(0, 0, -1)
  And shape_hit.inside = true
  # normal would have been (0, 0, 1), but is inverted!
  And shape_hit.normalv = vector(0, 0, -1)

Scenario: Precomputing the reflection vector
  Given p <- plane()
  And r <- ray(point(0, 1, -1), vector(0, -sqrt(2)/2, sqrt(2)/2))
  And i1 <- intersection(sqrt(2), p)
  When shape_hit <- hit(i1, r)
  Then shape_hit.reflectv = vector(0, sqrt(2)/2, sqrt(2)/2)

Scenario: The hit should offset the point
  Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s2 <- sphere() with:
    | variable  | value                |
    | transform | translation(0, 0, 1) |
  And i1 <- intersection(5, s2)
  When shape_hit <- hit(i1, r)
  Then shape_hit.over_point.z < -EPSILON/2
  And shape_hit.point.z > shape_hit.over_point.z

Scenario: The under point is offset below the surface
  Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s2 <- glass_sphere() with:
    | variable  | value                |
    | transform | translation(0, 0, 1) |
  And i1 <- intersection(5, s2)
  And xs <- intersections(i1)
  When shape_hit <- hit(i1, r, xs)
  Then shape_hit.under_point.z > EPSILON/2
  And shape_hit.point.z < shape_hit.under_point.z

Scenario Outline: Finding n1 and n2 at various intersections
  Given A <- glass_sphere() with:
    | variable  | value            |
    | transform | scaling(2, 2, 2) |
    | material.refractive_index | 1.5 |
  And B <- glass_sphere() with:
    | variable  | value            |
    | transform | translation(0, 0, -0.25) |
    | material.refractive_index | 2.0 |
  And C <- glass_sphere() with:
    | variable  | value            |
    | transform | translation(0, 0, 0.25) |
    | material.refractive_index | 2.5 |
  And r <- ray(point(0, 0, -4), vector(0, 0, 1))
  And xs <- intersections(2:A, 2.75:B, 3.25:C, 4.75:B, 5.25:C, 6:A)
  When shape_hit <- hit(xs[<index>], r, xs)
  Then shape_hit.n1 = <n1>
  And shape_hit.n2 = <n2>
    
  Examples:
    | index | n1 | n2 |
    | 0 | 1.0 | 1.5 |
    | 1 | 1.5 | 2.0 |
    | 2 | 2.0 | 2.5 |
    | 3 | 2.5 | 2.5 |
    | 4 | 2.5 | 1.5 |
    | 5 | 1.5 | 1.0 |

Scenario: The Schlick approximation under total internal reflection
  Given s <- glass_sphere()
  And r <- ray(point(0, 0, sqrt(2)/2), vector(0, 1, 0))
  And xs <- intersections(-sqrt(2)/2:s, sqrt(2)/2:s)
  When shape_hit <- hit(xs[1], r, xs)
  And reflectance <- schlick(shape_hit)
  Then reflectance = 1.0

Scenario: The Schlick approximation with a perpendicular viewing angle
  Given s <- glass_sphere()
  And r <- ray(point(0, 0, 0), vector(0, 1, 0))
  And xs <- intersections(-1:s, 1:s)
  When shape_hit <- hit(xs[1], r, xs)
  And reflectance <- schlick(shape_hit)
  Then reflectance = 0.04

Scenario: The Schlick approximation with small angle and n2 > n1
  Given s <- glass_sphere()
  And r <- ray(point(0, 0.99, -2), vector(0, 0, 1))
  And xs <- intersections(1.8589:s)
  When shape_hit <- hit(xs[0], r, xs)
  And reflectance <- schlick(shape_hit)
  Then reflectance = 0.48873

