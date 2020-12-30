Feature: Cylinder

  Scenario Outline: A ray misses a cylinder
    Given c <- cylinder()
    And r <- ray(<origin>, <direction>)
    When xs <- local_intersect(c, r)
    Then xs.count = 0
    
    Examples:
      | origin          | direction                               |
      | point(1, 0, 0)  | vector(0, 1, 0)                         |
      | point(0, 0, 0)  | vector(0, 1, 0)                         |
      | point(0, 0, -5) | vector(0.5773502, 0.5773502, 0.5773502) |

  Scenario Outline: A ray strikes a cylinder
    Given c <- cylinder()
    And r <- ray(<origin>, <direction>)
    When xs <- local_intersect(c, r)
    Then xs.count = 2
    And xs[0].t = <t0>
    And xs[1].t = <t1>

    Examples:
      | origin            | direction                               | t0      | t1      |
      | point(1, 0, -5)   | vector(0, 0, 1)                         | 5       | 5       |
      | point(0, 0, -5)   | vector(0, 0, 1)                         | 4       | 6       |
      | point(0.5, 0, -5) | vector(0.0705345, 0.7053456, 0.7053456) | 6.80798 | 7.08872 |

  Scenario Outline: Normal vector on a cylinder
    Given c <- cylinder()
    And p <- <point>
    When normal <- local_normal_at(c, p)
    Then normal = <normal>

    Examples:
      | point           | normal           |
      | point(1, 0, 0)  | vector(1, 0, 0)  |
      | point(0, 5, -1) | vector(0, 0, -1) |
      | point(0, -2, 1) | vector(0, 0, 1)  |
      | point(-1, 1, 0) | vector(-1, 0, 0) |

  Scenario: The default minimum and maximum for a cylinder
    Given c <- cylinder()
    Then c.minimum = -infinity
    And c.maximum = infinity

  Scenario Outline: Intersecting a constrained cylinder
    Given c <- cylinder()
    And c.minimum <- 1
    And c.maximum <- 2
    And r <- ray(<point>, <direction>)
    When xs <- local_intersect(c, r)
    Then xs.count = <count>

    Examples:
      |   | point             | direction                       | count |
      | 1 | point(0, 1.5, 0)  | vector(0.0995037, 0.9950371, 0) | 0     |
      | 2 | point(0, 3, -5)   | vector(0, 0, 1)                 | 0     |
      | 3 | point(0, 0, -5)   | vector(0, 0, 1)                 | 0     |
      | 4 | point(0, 2, -5)   | vector(0, 0, 1)                 | 0     |
      | 5 | point(0, 1, -5)   | vector(0, 0, 1)                 | 0     |
      | 6 | point(0, 1.5, -2) | vector(0, 0, 1)                 | 2     |

  Scenario: The default closed value for a cylinder
    Given c <- cylinder()
    Then c.closed = false

  Scenario Outline: Intersecting the caps of a closed cylinder
    Given c <- cylinder()
    And c.minimum <- 1
    And c.maximum <- 2
    And c.closed <- true
    And r <- ray(<point>, <direction>)
    When xs <- local_intersect(c, r)
    Then xs.count = <count>
    
    Examples:
      |   | point            | direction                        | count |
      | 1 | point(0, 3, 0)   | vector(0, -1, 0)                 | 2     |
      | 2 | point(0, 3, -2)  | vector(0, -0.4472135, 0.8944271) | 2     |
      | 3 | point(0, 4, -2)  | vector(0, -0.7071067, 0.7071067) | 2     | 
      | 4 | point(0, 0, -2)  | vector(0, 0.4472135, 0.8944271)  | 2     |
      | 5 | point(0, -1, -2) | vector(0, 0.7071067, 0.7071067)  | 2     |

  Scenario Outline: The normal vector on a cylinder's end caps
    Given c <- cylinder()
    And c.minimum <- 1
    And c.maximum <- 2
    And c.closed <- true
    And p <- <point>
    When normal <- local_normal_at(c, p)
    Then normal = <normal>

    Examples:
      | point            | normal           |
      | point(0, 1, 0)   | vector(0, -1, 0) |
      | point(0.5, 1, 0) | vector(0, -1, 0) |
      | point(0, 1, 0.5) | vector(0, -1, 0) |
      | point(0, 2, 0)   | vector(0, 1, 0)  |
      | point(0.5, 2, 0) | vector(0, 1, 0)  |
      | point(0, 2, 0.5) | vector(0, 1, 0)  |

