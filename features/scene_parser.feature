Feature: Scene Parser

  Scenario: Add camera to scene
    Given data <- yaml:
    """
    - add: camera
      width: 160
      height: 100
      field-of-view: 1.570796
      from: [0, 0, -5]
      to: [0, 0.5, 0]
      up: [0, 1, 0]
    """
    When c <- scene_from_yaml(data)
    Then c.hsize = 160
    And c.vsize = 100
    And c.field_of_view = pi/2

  Scenario: Adds light source to world
    Given data <- yaml:
    """
    - add: light
      at: [-10, 10, -10]
      intensity: [1, 1, 1]
    """
    And light <- point_light(point(-10, 10, -10), color(1, 1, 1))
    When w <- scene_from_yaml(data)
    Then w.light = light 

  Scenario: Adds shape to world
    Given data <- yaml:
    """
    - add: sphere
      material:
        color: [1, 0.3, 0.2]
    """
    When w <- scene_from_yaml(data)
    Then w.objects.count = 1
    And w.objects[0].material.color = color(1, 0.3, 0.2)

  Scenario: Uses definied transformation for shape
    Given data <- yaml:
    """
    - define: std-transform
      value:
        - [ translate, 1, -1, 1 ]
    - add: sphere
      transform:
        - std-transform
        - [ scale, 5, 5, 5 ]
    """
    When w <- scene_from_yaml(data)
    Then w.objects[0].transform = scaling(5, 5, 5) * translation(1, -1, 1)

  Scenario: Uses definied material for shape
    Given data <- yaml:
    """
    - define: blue-material
      value:
         color: [0.5, 0.5, 1.0]
         ambient: 1
    - add: sphere
      material: blue-material
    """
    When w <- scene_from_yaml(data)
    Then w.objects[0].material.color = color(0.5, 0.5, 1.0)
    And w.objects[0].material.ambient = 1
