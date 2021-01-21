Feature: materials

Background:
  Given m <- material()
  And s <- sphere()
  And p <- point(0, 0, 0)

Scenario: The default material
  Given m <- material()
  Then m.color = color(1, 1, 1)
  And m.ambient = 0.1
  And m.diffuse = 0.9
  And m.specular = 0.9
  And m.shininess = 200.0

Scenario: Creating a material from yaml
  Given data <- yaml:
  """"
  material:
    color: [0.9, 0.4, 0.6]
    ambient: 0.2
    diffuse: 0.1
    specular: 0.3
    shininess: 300
    reflective: 0.1
    transparency: 0.4
    refractive-index: 1.5
  """"
  When m <- Material.from_yaml(data)
  Then m.color = color(0.9, 0.4, 0.6)
  And m.ambient = 0.2
  And m.diffuse = 0.1
  And m.specular = 0.3
  And m.shininess = 300.0
  And m.reflective = 0.1
  And m.transparency = 0.4
  And m.refractive_index = 1.5

Scenario: Creating a material with stripe pattern from yaml
  Given data <- yaml:
  """
  material:
     pattern:
       type: stripes
       colors:
         - [1, 1, 1]
         - [0, 0, 0]
  """
  When m <- Material.from_yaml(data)
  Then m.pattern = stripe_pattern(color(1, 1, 1), color(0, 0, 0))

Scenario: Creating a material with checkers pattern from yaml
  Given data <- yaml:
  """
  material:
     pattern:
       type: checkers
       colors:
         - [1, 1, 1]
         - [0, 0, 0]
  """
  When m <- Material.from_yaml(data)
  Then m.pattern = checkers_pattern(color(1, 1, 1), color(0, 0, 0))

Scenario: Creating a material with ring pattern from yaml
  Given data <- yaml:
  """
  material:
     pattern:
       type: ring
       colors:
         - [1, 1, 1]
         - [0, 0, 0]
  """
  When m <- Material.from_yaml(data)
  Then m.pattern = ring_pattern(color(1, 1, 1), color(0, 0, 0))

Scenario: Creating a material with gradient pattern from yaml
  Given data <- yaml:
  """
  material:
     pattern:
       type: gradient
       colors:
         - [1, 1, 1]
         - [0, 0, 0]
  """
  When m <- Material.from_yaml(data)
  Then m.pattern = gradient_pattern(color(1, 1, 1), color(0, 0, 0))

Scenario: Lighting with the eye between the light and the surface
  Given v1 <- vector(0, 0, -1)
  And v2 <- vector(0, 0, -1)
  And light <- point_light(point(0, 0, -10), color(1, 1, 1))
  When c <- lighting(m, s, light, p, v1, v2)
  Then c = color(1.9, 1.9, 1.9)

Scenario: Lighting with the eye between light and surface, eye offset 45°
  Given v1 <- vector(0, sqrt(2)/2, -sqrt(2)/2)
  And v2 <- vector(0, 0, -1)
  And light <- point_light(point(0, 0, -10), color(1, 1, 1))
  When c <- lighting(m, s, light, p, v1, v2)
  Then c = color(1.0, 1.0, 1.0)

Scenario: Lighting with eye opposite surface, light offset 45°
  Given v1 <- vector(0, 0, -1)
  And v2 <- vector(0, 0, -1)
  And light <- point_light(point(0, 10, -10), color(1, 1, 1))
  When c <- lighting(m, s, light, p, v1, v2)
  Then c = color(0.7364, 0.7364, 0.7364)

Scenario: Lighting with eye in the path of the reflection vector
  Given v1 <- vector(0, -sqrt(2)/2, -sqrt(2)/2)
  And v2 <- vector(0, 0, -1)
  And light <- point_light(point(0, 10, -10), color(1, 1, 1))
  When c <- lighting(m, s, light, p, v1, v2)
  Then c = color(1.6364, 1.6364, 1.6364)

Scenario: Lighting with the light behind the surface
  Given v1 <- vector(0, 0, -1)
  And v2 <- vector(0, 0, -1)
  And light <- point_light(point(0, 0, 10), color(1, 1, 1))
  When c <- lighting(m, s, light, p, v1, v2)
  Then c = color(0.1, 0.1, 0.1)

Scenario: Lighting with the surface in shadow
  Given v1 <- vector(0, 0, -1)
  And v2 <- vector(0, 0, -1)
  And light <- point_light(point(0, 0, -10), color(1, 1, 1))
  When c <- lighting(m, s, light, p, v1, v2, 0.0)
  Then c = color(0.1, 0.1, 0.1)

Scenario: Lighting with a pattern applied
  Given m.pattern <- stripe_pattern(color(1, 1, 1), color(0, 0, 0))
  And m.ambient <- 1
  And m.diffuse <- 0
  And m.specular <- 0
  And p1 <- point(0.9, 0, 0)
  And p2 <- point(1.1, 0, 0)
  And v1 <- vector(0, 0, -1)
  And v2 <- vector(0, 0, -1)
  And light <- point_light(point(0, 0, -10), color(1, 1, 1))
  When c <- lighting(m, s, light, p1, v1, v2, 0.0)
  And c2 <- lighting(m, s, light, p2, v1, v2, 0.0)
  Then c = color(1, 1, 1)
  And c2 = color(0, 0, 0)

Scenario: Reflectivity for the default material
  Given m <- material()
  Then m.reflective = 0.0

Scenario: Transparency and Refractive Index for the default material
  Given m <- material()
  Then m.transparency = 0.0
  And m.refractive_index = 1.0

  Scenario Outline: lighting() uses light intensity to attenuate color
    Given w <- default_world()
    And light <- point_light(point(0, 0, -10), color(1, 1, 1))
    And s1 <- the first object in w
    And m.ambient <- 0.1
    And m.diffuse <- 0.9
    And m.specular <- 0
    And m.color <- color(1, 1, 1)
    And p <- point(0, 0, -1)
    And v1 <- vector(0, 0, -1)
    And v2 <- vector(0, 0, -1)
    When w.lights[0] <- light
    And c <- lighting(m, s1, light, p, v1, v2, <intensity>)
    Then c = <result>

    Examples:
      | intensity | result                  |
      | 1.0       | color(1, 1, 1)          |
      | 0.5       | color(0.55, 0.55, 0.55) |
      | 0.0       | color(0.1, 0.1, 0.1)    |

  Scenario Outline: lighting() samples the area light
    Given corner <- point(-0.5, -0.5, -5)
    And v1 <- vector(1, 0, 0)
    And v2 <- vector(0, 1, 0)
    And light <- area_light(corner, v1, 2, v2, 2, color(1, 1, 1))
    And m.ambient <- 0.1
    And m.diffuse <- 0.9
    And m.specular <- 0
    And m.color <- color(1, 1, 1)
    And eye <- point(0, 0, -5)
    And p <- <point>
    And v1 <- normalize(eye - p)
    And v2 <- vector(p.x, p.y, p.z)
    When c <- lighting(m, s, light, p, v1, v2, 1.0)
    Then c = <result>

    Examples:
      | point                      | result                        |
      | point(0, 0, -1)            | color(0.9965, 0.9965, 0.9965) |
      | point(0, 0.7071, -0.7071)  | color(0.62318, 0.62318, 0.62318) |
      #book: | point(0, 0.7071, -0.7071)  | color(0.6232, 0.6232, 0.6232) |
