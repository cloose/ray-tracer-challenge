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

