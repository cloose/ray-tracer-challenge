Feature: Cones

  Scenario Outline: Intersecting a cone with a ray
    Given c <- cone()
    And r <- ray(<origin>, <direction>)
    When xs <- local_intersect(c, r)
    Then xs.count = 2
    And xs[0].t = <t0>
    And xs[1].t = <t1>
    Examples:
      | origin | direction | t0 | t1 |
      | point(0, 0, -5) | vector(0, 0, 1) | 5 | 5 |
      | point(0, 0, -5) | vector(0.5773502, 0.5773502, 0.5773502) | 8.66025 | 8.66025 |
      | point(1, 1, -5) | vector(-0.3333333, -0.6666666, 0.6666666) | 4.55006 | 49.44994 |

  Scenario: Intersecting a cone with a ray parallel to one of its halves
    Given c <- cone()
    And r <- ray(point(0, 0, -1), vector(0.0, 0.7071067, 0.7071067))
    When xs <- local_intersect(c, r)
    Then xs.count = 1
    And xs[0].t = 0.35355

  Scenario Outline: Intersecting a cone's end caps
    Given c <- cone()
    And c.minimum <- -0.5
    And c.maximum <- 0.5
    And c.closed <- true
    And r <- ray(<origin>, <direction>)
    When xs <- local_intersect(c, r)
    Then xs.count = <count>
    Examples:
      | origin | direction | count |
      | point(0, 0, -5) | vector(0, 1, 0) | 0 |
      | point(0, 0, -0.25) | vector(0.0, 0.7071067, 0.7071067) | 2 |
      | point(0, 0, -0.25) | vector(0, 1, 0) | 4 |

  Scenario Outline: Computing the normal vector on a cone
    Given c <- cone()
    And p <- <point>
    When normal <- local_normal_at(c, p)
    Then normal = <normal>
    Examples:
      | point | normal |
      | point(0, 0, 0) | vector(0, 0, 0) |
      | point(1, 1, 1) | vector(1, -sqrt(2), 1) |
      | point(-1, -1, 0) | vector(-1, 1, 0) |

