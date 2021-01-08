Feature: world

Scenario: Creating a world
  Given w <- world()
  Then w contains no objects
  And w has no light source

Scenario: The default world
  Given light <- point_light(point(-10, 10, -10), color(1, 1, 1))
  And s1 <- sphere() with:
    | variable          | value           |
    | material.color    | (0.8, 1.0, 0.6) |
    | material.diffuse  | 0.7             |
    | material.specular | 0.2             |
  And s2 <- sphere() with:
    | variable  | value                  |
    | transform | scaling(0.5, 0.5, 0.5) |
  And w <- default_world()
  Then w.lights[0] = light
   And w contains s1
   And w contains s2

Scenario: Intersect a world with a ray
  Given w <- default_world()
  And r <- ray(point(0, 0, -5), vector(0, 0, 1))
  When xs <- intersect_world(w, r)
  Then xs.count = 4
  And xs[0].t = 4
  And xs[1].t = 4.5
  And xs[2].t = 5.5
  And xs[3].t = 6

Scenario: Shading an intersection
  Given w <- default_world()
  And r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s1 <- the first object in w
  And i1 <- intersection(4, s1)
  When shape_hit <- hit(i1, r)
  And c <- shade_hit(w, shape_hit)
  Then c = color(0.38066, 0.47583, 0.2855)

Scenario: Shading an intersection from the inside
  Given w <- default_world()
  And light <- point_light(point(0, 0.25, 0), color(1, 1, 1))
  And r <- ray(point(0, 0, 0), vector(0, 0, 1))
  And s2 <- the second object in w
  And i1 <- intersection(0.5, s2)
  When shape_hit <- hit(i1, r)
  And w.lights[0] <- light
  And c <- shade_hit(w, shape_hit)
  Then c = color(0.90498, 0.90498, 0.90498)

Scenario: Shading an intersection with two lights
  Given w <- default_world()
  And light <- point_light(point(10, 10, 10), color(0.1, 0.1, 0.1))
  And r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And s1 <- the first object in w
  And i1 <- intersection(4, s1)
  When w.add_light(light)
  When shape_hit <- hit(i1, r)
  And c <- shade_hit(w, shape_hit)
  Then c = color(0.38866, 0.48583, 0.29149)

Scenario: The color when a ray misses
  Given w <- default_world()
  And r <- ray(point(0, 0, -5), vector(0, 1, 0))
  When c <- color_at(w, r)
  Then c = color(0, 0, 0)

Scenario: The color when a ray hits
  Given w <- default_world()
  And r <- ray(point(0, 0, -5), vector(0, 0, 1))
  When c <- color_at(w, r)
  Then c = color(0.38066, 0.47583, 0.2855)

Scenario: The color with an intersection behind the ray
  Given w <- default_world()
  And s1 <- the first object in w
  And s1.material.ambient <- 1
  And s2 <- the second object in w
  And s2.material.ambient <- 1
  And r <- ray(point(0, 0, 0.75), vector(0, 0, -1))
  When c <- color_at(w, r)
  Then c = s2.material.color

Scenario: There is no shadow when nothing is collinear with point and light
  Given w <- default_world()
  And p <- point(0, 10, 0)
  Then is_shadowed(w, p, w.lights[0]) is false

Scenario: The shadow when an object is between the point and the light
  Given w <- default_world()
  And p <- point(10, -10, 10)
  Then is_shadowed(w, p, w.lights[0]) is true

Scenario: There is no shadow when an object is behind the light
  Given w <- default_world()
  And p <- point(-20, 20, -20)
  Then is_shadowed(w, p, w.lights[0]) is false

Scenario: There is no shadow when an object is behind the point
  Given w <- default_world()
  And p <- point(-2, 2, -2)
  Then is_shadowed(w, p, w.lights[0]) is false

Scenario: shade_hit() is given an intersection in shadow
  Given w <- world()
  And light <- point_light(point(0, 0.25, 0), color(1, 1, 1))
  And s <- sphere()
  And s is added to w
  And s2 <- sphere() with:
    | variable  | value                 |
    | transform | translation(0, 0, 10) |
  And s2 is added to w
  And r <- ray(point(0, 0, 5), vector(0, 0, 1))
  And i1 <- intersection(4, s2)
  When shape_hit <- hit(i1, r)
  And w.add_light(light)
  And c <- shade_hit(w, shape_hit)
  Then c = color(0.1, 0.1, 0.1)

Scenario: The reflected color for a nonreflective material
  Given w <- default_world()
  And r <- ray(point(0, 0, 0), vector(0, 0, 1))
  And s2 <- the second object in w
  And s2.material.ambient <- 1
  And i1 <- intersection(1, s2)
  When shape_hit <- hit(i1, r)
  And c <- reflected_color(w, shape_hit)
  Then c = color(0, 0, 0)

Scenario: The reflected color for a reflective material
  Given w <- default_world()
  And p <- plane() with:
    | variable  | value                 |
    | material.reflective | 0.5 |
    | transform | translation(0, -1, 0) |
  And p is added to w
  And r <- ray(point(0, 0, -3), vector(0, -sqrt(2)/2, sqrt(2)/2))
  And i1 <- intersection(sqrt(2), p)
  When shape_hit <- hit(i1, r)
  And c <- reflected_color(w, shape_hit)
  # book: Then c = color(0.19032, 0.2379, 0.14274)
  Then c = color(0.19033, 0.23791, 0.14274)

Scenario: shade_hit() with a reflective material
  Given w <- default_world()
  And p <- plane() with:
    | variable  | value                 |
    | material.reflective | 0.5 |
    | transform | translation(0, -1, 0) |
  And p is added to w
  And r <- ray(point(0, 0, -3), vector(0, -sqrt(2)/2, sqrt(2)/2))
  And i1 <- intersection(sqrt(2), p)
  When shape_hit <- hit(i1, r)
  And c <- shade_hit(w, shape_hit)
  # book: Then c = color(0.87677, 0.92436, 0.82918)
  Then c = color(0.87675, 0.92434, 0.82918)

Scenario: color_at() with mutually reflective surfaces
  Given w <- world()
  And light <- point_light(point(0, 0, 0), color(1, 1, 1))
  And p <- plane() with:
    | variable  | value                 |
    | material.reflective | 1 |
    | transform | translation(0, -1, 0) |
  And p is added to w
  And p2 <- plane() with:
    | variable  | value                 |
    | material.reflective | 1 |
    | transform | translation(0, 1, 0) |
  And p2 is added to w
  And r <- ray(point(0, 0, 0), vector(0, 1, 0))
  When w.add_light(light)
  Then color_at(w, r) should terminate successfully

Scenario: The reflected color at the maximum recursive depth
  Given w <- default_world()
  And p <- plane() with:
    | variable  | value                 |
    | material.reflective | 0.5 |
    | transform | translation(0, -1, 0) |
  And p is added to w
  And r <- ray(point(0, 0, -3), vector(0, -sqrt(2)/2, sqrt(2)/2))
  And i1 <- intersection(sqrt(2), p)
  When shape_hit <- hit(i1, r)
  And c <- reflected_color(w, shape_hit, 0)
  Then c = color(0, 0, 0)

Scenario: The refracted color with an opaque surface
  Given w <- default_world()
  And s1 <- the first object in w
  And r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And xs <- intersections(4:s1, 6:s1)
  When shape_hit <- hit(xs[0], r, xs)
  And c <- refracted_color(w, shape_hit, 5)
  Then c = color(0, 0, 0)

Scenario: The refracted color at the maximum recursive depth
  Given w <- default_world()
  And s1 <- the first object in w
  And s1 has:
    | variable  | value                 |
    | material.transparency | 1.0 |
    | material.refractive_index | 1.5 |
  And r <- ray(point(0, 0, -5), vector(0, 0, 1))
  And xs <- intersections(4:s1, 6:s1)
  When shape_hit <- hit(xs[0], r, xs)
  And c <- refracted_color(w, shape_hit, 0)
  Then c = color(0, 0, 0)

Scenario: The refracted color under total internal reflection
  Given w <- default_world()
  And s1 <- the first object in w
  And s1 has:
    | variable  | value                 |
    | material.transparency | 1.0 |
    | material.refractive_index | 1.5 |
  And r <- ray(point(0, 0, sqrt(2)/2), vector(0, 1, 0))
  And xs <- intersections(-sqrt(2)/2:s1, sqrt(2)/2:s1)
  # NOTE: this time you're inside the sphere, so you need
  # to look at the second intersection, xs[1], not xs[0]
  When shape_hit <- hit(xs[1], r, xs)
  And c <- refracted_color(w, shape_hit, 5)
  Then c = color(0, 0, 0)

Scenario: The refracted color with a refracted ray
  Given w <- default_world()
  And s1 <- the first object in w
  And s1 has:
    | variable  | value                 |
    | material.ambient | 1.0 |
    | material.pattern | test_pattern() |
  And s2 <- the second object in w
  And s2 has:
    | variable  | value                 |
    | material.transparency | 1.0 |
    | material.refractive_index | 1.5 |
  And r <- ray(point(0, 0, 0.1), vector(0, 1, 0))
  And xs <- intersections(-0.9899:s1, -0.4899:s2, 0.4899:s2, 0.9899:s1)
  When shape_hit <- hit(xs[2], r, xs)
  And c <- refracted_color(w, shape_hit, 5)
  # book: Then c = color(0, 0.99888, 0.04725)
  Then c = color(0, 0.99888, 0.04722)

Scenario: shade_hit() with a transparent material
  Given w <- default_world()
  And p <- plane() with:
    | variable  | value                 |
    | transform | translation(0, -1, 0) |
    | material.transparency | 0.5 |
    | material.refractive_index | 1.5 |
  And p is added to w
  And s2 <- sphere() with:
    | variable  | value                 |
    | material.color | (1, 0, 0) |
    | material.ambient | 0.5 |
    | transform | translation(0, -3.5, -0.5) |
  And s2 is added to w
  And r <- ray(point(0, 0, -3), vector(0, -sqrt(2)/2, sqrt(2)/2))
  And xs <- intersections(sqrt(2):p)
  When shape_hit <- hit(xs[0], r, xs)
  And c <- shade_hit(w, shape_hit, 5)
  Then c = color(0.93642, 0.68642, 0.68642)


Scenario: shade_hit() with a reflective, transparent material
  Given w <- default_world()
  And r <- ray(point(0, 0, -3), vector(0, -sqrt(2)/2, sqrt(2)/2))
  And p <- plane() with:
    | variable  | value                 |
    | transform | translation(0, -1, 0) |
    | material.reflective | 0.5 |
    | material.transparency | 0.5 |
    | material.refractive_index | 1.5 |
  And p is added to w
  And s2 <- sphere() with:
    | variable  | value                 |
    | material.color | (1, 0, 0) |
    | material.ambient | 0.5 |
    | transform | translation(0, -3.5, -0.5) |
  And s2 is added to w
  And xs <- intersections(sqrt(2):p)
  When shape_hit <- hit(xs[0], r, xs)
  And c <- shade_hit(w, shape_hit, 5)
  Then c = color(0.93391, 0.69643, 0.69243)

