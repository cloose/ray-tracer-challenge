Feature: lights

  Scenario: A point light has a position and intensity
    Given c <- color(1, 1, 1)
    And p <- point(0, 0, 0)
    When light <- point_light(p, c)
    Then light.position = p
    And light.intensity = c

  Scenario: Creating a point light from yaml
    Given data <- yaml:
    """
    add: light
    at: [-4.9, 4.9, -1]
    intensity: [1, 1, 1]
    """
    When light <- PointLight.from_yaml(data)
    Then light.position = point(-4.9, 4.9, -1)
    And light.intensity = color(1, 1, 1)
