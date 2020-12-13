Feature: lights

Scenario: A point light has a position and intensity
  Given c <- color(1, 1, 1)
  And p <- point(0, 0, 0)
  When light <- point_light(p, c)
  Then light.position = p
  And light.intensity = c
