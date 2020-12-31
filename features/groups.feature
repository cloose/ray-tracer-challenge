Feature: Groups

  Scenario: Creating a new group
    Given g <- group()
    Then g.transform = identity_matrix
    And g is empty

  Scenario: Adding a child to a group
    Given g <- group()
    And s <- test_shape()
    When add_child(g, s)
    Then g is not empty
    And g includes s
    And s.parent = g

  Scenario: Intersecting a ray with an empty group
    Given g <- group()
    And r <- ray(point(0, 0, 0), vector(0, 0, 1))
    When xs <- local_intersect(g, r)
    Then xs is empty

  Scenario: Intersecting a ray with a nonempty group
    Given g <- group()
    And s <- sphere()
    And s2 <- sphere() with:
      | variable  | value                 |
      | transform | translation(0, 0, -3) |
    And s3 <- sphere() with:
      | variable  | value                 |
      | transform | translation(5, 0, 0)  |
    And r <- ray(point(0, 0, -5), vector(0, 0, 1))
    When add_child(g, s)
    And add_child(g, s2)
    And add_child(g, s3)
    And xs <- local_intersect(g, r)
    Then xs.count = 4
    And xs[0].object = s2
    And xs[1].object = s2
    And xs[3].object = s
    And xs[2].object = s

  Scenario: Intersecting a transformed group
    Given g <- group()
    And s <- sphere()
    And r <- ray(point(10, 0, -10), vector(0, 0, 1))
    When add_child(g, s)
    And set_transform(g, scaling(2, 2, 2))
    And set_transform(s, translation(5, 0, 0))
    And xs <- intersect(g, r)
    Then xs.count = 2
