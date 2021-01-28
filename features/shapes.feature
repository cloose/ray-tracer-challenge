Feature: shapes

  Scenario: A shape has a parent attribute
    Given s <- test_shape()
    Then s.parent is nothing

  Scenario: A shape A includes another shape if same instance
    Given A <- test_shape()
    And B <- test_shape()
    Then A includes A
    And A not includes B

  Scenario: A shape casts a shadow by default
    Given s <- test_shape()
    Then s.cast_shadow = true

  Scenario: A shape's default transformation
    Given s <- test_shape()
    Then s.transform = identity_matrix

  Scenario: Assigning a transformation
    Given s <- test_shape()
    When set_transform(s, translation(2, 3, 4))
    Then s.transform = translation(2, 3, 4)

  Scenario: A shape has a default material
    Given s <- test_shape()
    Then s.material = material()

  Scenario: Assigning a material
    Given s <- test_shape()
    And m <- material()
    And m.ambient <- 1
    When s.material <- m
    Then s.material = m

  Scenario: Intersecting a scaled shape with a ray
    Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
    And s <- test_shape()
    When set_transform(s, scaling(2, 2, 2))
    And xs <- intersect(s, r)
    Then s.saved_ray.origin = point(0, 0, -2.5)
    And s.saved_ray.direction = vector(0, 0, 0.5)

  Scenario: Intersecting a translated shape with a ray
    Given r <- ray(point(0, 0, -5), vector(0, 0, 1))
    And s <- test_shape()
    When set_transform(s, translation(5, 0, 0))
    And xs <- intersect(s, r)
    Then s.saved_ray.origin = point(-5, 0, -5)
    And s.saved_ray.direction = vector(0, 0, 1)

  Scenario: Computing the normal on a translated shape
    Given s <- test_shape()
    When set_transform(s, translation(0, 1, 0))
    And n <- normal_at(s, point(0, 1.70711, -0.70711))
    Then n = vector(0, 0.70711, -0.70711)
    
  Scenario: Computing the normal on a transformed shape
    Given s <- test_shape()
    And m <- scaling(1, 0.5, 1) * rotation_z(pi/5)
    When set_transform(s, m)
    And n <- normal_at(s, point(0, sqrt(2)/2, -sqrt(2)/2))
    Then n = vector(0, 0.97014, -0.24254)

  Scenario: The normal is a normalized vector
    Given s <- test_shape()
    When n <- normal_at(s, point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
    Then n = normalize(n)

  Scenario: Converting a point from world to object space
    Given g1 <- group()
    And g2 <- group()
    And s <- sphere()
    When add_child(g1, g2)
    And add_child(g2, s)
    And set_transform(g1, rotation_y(pi/2))
    And set_transform(g2, scaling(2, 2, 2))
    And set_transform(s, translation(5, 0, 0))
    And p <- world_to_object(s, point(-2, 0, -10))
    Then p = point(0, 0, -1)

  Scenario: Converting a normal from object to world space
    Given g1 <- group()
    And g2 <- group()
    And s <- sphere()
    When add_child(g1, g2)
    And add_child(g2, s)
    And set_transform(g1, rotation_y(pi/2))
    And set_transform(g2, scaling(1, 2, 3))
    And set_transform(s, translation(5, 0, 0))
    And n <- normal_to_world(s, vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
    # book: Then n = vector(0.2857, 0.4286, -0.8571)
    Then n = vector(0.28571, 0.42857, -0.85714)

  Scenario: Finding the normal on a child object
    Given g1 <- group()
    And g2 <- group()
    And s <- sphere()
    When add_child(g1, g2)
    And add_child(g2, s)
    And set_transform(g1, rotation_y(pi/2))
    And set_transform(g2, scaling(1, 2, 3))
    And set_transform(s, translation(5, 0, 0))
    When n <- normal_at(s, point(1.7321, 1.1547, -5.5774))
    # book: Then n = vector(0.2857, 0.4286, -0.8571)
    Then n = vector(0.2857, 0.42854, -0.85716)
