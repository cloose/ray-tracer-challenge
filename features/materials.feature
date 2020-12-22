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
  """"
  When m <- Material.from_yaml(data)
  Then m.color = color(0.9, 0.4, 0.6)
  And m.ambient = 0.2
  And m.diffuse = 0.1
  And m.specular = 0.3

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
  When c <- lighting(m, s, light, p, v1, v2, in_shadow)
  Then c = color(0.1, 0.1, 0.1)

Scenario: Lighting with a pattern applied
  Given m.pattern <- stripe_pattern(color(1, 1, 1), color(0, 0, 0))
  And m.ambient <- 1
  And m.diffuse <- 0
  And m.specular <- 0
  And v1 <- vector(0, 0, -1)
  And v2 <- vector(0, 0, -1)
  And light <- point_light(point(0, 0, -10), color(1, 1, 1))
  When c1 <- lighting(m, s, light, point(0.9, 0, 0), v1, v2, false)
  And c2 <- lighting(m, s, light, point(1.1, 0, 0), v1, v2, false)
  Then c1 = color(1, 1, 1)
  And c2 = color(0, 0, 0)

Scenario: Reflectivity for the default material
  Given m <- material()
  Then m.reflective = 0.0

Scenario: Transparency and Refractive Index for the default material
  Given m <- material()
  Then m.transparency = 0.0
  And m.refractive_index = 1.0
