Feature: camera

Scenario: Constructing a camera
  Given c <- camera(160, 120, pi/2)
  Then c.hsize = 160
  And c.vsize = 120
  And c.field_of_view = pi/2
  And c.transform = identity_matrix

Scenario: Creating a camera from yaml
  Given data <- yaml:
  """
  add: camera
  width: 160
  height: 120
  field-of-view: 1.570796
  from: [0, 0, -5]
  to: [0, 0.5, 0]
  up: [0, 1, 0]
  """
  And p <- point(0, 0, -5)
  And to <- point(0, 0.5, 0)
  And up <- vector(0, 1, 0)
  When c <- Camera.from_yaml(data)
  Then c.hsize = 160
  And c.vsize = 120
  And c.field_of_view = pi/2
  And c.transform = view_transform(p, to, up)

Scenario: The pixel size for a horizontal canvas
  Given c <- camera(200, 125, pi/2)
  Then c.pixel_size = 0.01

Scenario: The pixel size for a vertical canvas
  Given c <- camera(125, 200, pi/2)
  Then c.pixel_size = 0.01

Scenario: Constructing a ray through the center of the canvas
  Given c <- camera(201, 101, pi/2)
  When r2 <- ray_for_pixel(c, 100, 50)
  Then r2.origin = point(0, 0, 0)
  And r2.direction = vector(0, 0, -1)

Scenario: Constructing a ray through a corner of the canvas
  Given c <- camera(201, 101, pi/2)
  When r2 <- ray_for_pixel(c, 0, 0)
  Then r2.origin = point(0, 0, 0)
  And r2.direction = vector(0.66519, 0.33259, -0.66851)

Scenario: Constructing a ray when the camera is transformed
  Given c <- camera(201, 101, pi/2)
  When c.transform <- rotation_y(pi/4) * translation(0, -2, 5)
  And r2 <- ray_for_pixel(c, 100, 50)
  Then r2.origin = point(0, 2, -5)
  And r2.direction = vector(sqrt(2)/2, 0, -sqrt(2)/2)

Scenario: Rendering a world with a camera
  Given w <- default_world()
  And c <- camera(11, 11, pi/2)
  And p <- point(0, 0, -5)
  And to <- point(0, 0, 0)
  And up <- vector(0, 1, 0)
  When A <- view_transform(p, to, up)
  And c.transform <- A
  And image <- render(c, w)
  Then pixel_at(image, 5, 5) = color(0.38066, 0.47583, 0.2855)

