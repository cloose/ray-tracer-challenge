from core import point
from shapes import Group, Triangle, Material
from .obj_file import ObjFile


def parse_obj_file(content, material=Material()):
    obj_file = ObjFile()

    current_group = obj_file.groups["default"]

    for line in content:
        parts = line.split()

        if len(parts) < 1:
            obj_file.ignored += 1
            continue

        if parts[0] == "v":
            obj_file.vertices.append(
                point(float(parts[1]), float(parts[2]), float(parts[3])))
        elif parts[0] == "g":
            current_group = Group()
            obj_file.groups[parts[1]] = current_group
        elif parts[0] == "f":
            vertices = [None]
            for index in range(1, len(parts)):
                i = to_int(parts[index])
                vertices.append(obj_file.vertices[i])

            triangles = fan_triangulation(vertices, material)

            for triangle in triangles:
                current_group.add_child(triangle)
        else:
            obj_file.ignored += 1

    return obj_file


def to_int(index):
    parts = index.split('/')
    return int(parts[0])


# vertices is a 1-based array of at least three vertices
def fan_triangulation(vertices, material):
    triangles = []

    for index in range(2, len(vertices) - 1):
        tri = Triangle(vertices[1], vertices[index], vertices[index + 1])
        tri.material = material
        triangles.append(tri)

    return triangles
