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

