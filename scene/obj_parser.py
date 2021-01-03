from core import point, vector
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
        elif parts[0] == "vn":
            obj_file.normals.append(
                vector(float(parts[1]), float(parts[2]), float(parts[3])))
        elif parts[0] == "g":
            current_group = Group()
            obj_file.groups[parts[1]] = current_group
        elif parts[0] == "f":
            vertices = [None]
            normals = [None]
            for index in range(1, len(parts)):
                v, vt, vn = to_ints(parts[index])
                vertices.append(obj_file.vertices[v])
                if vn:
                    normals.append(obj_file.normals[vn])

            triangles = fan_triangulation(vertices, normals, material)

            for triangle in triangles:
                current_group.add_child(triangle)
        else:
            obj_file.ignored += 1

    return obj_file


def to_ints(index):
    parts = index.split('/')

    v = int(parts[0])

    vt = None
    if len(parts) > 1 and parts[1]:
        vt = int(parts[1])

    vn = None
    if len(parts) > 1 and parts[2]:
        vn = int(parts[2])

    return (v, vt, vn)


# vertices is a 1-based array of at least three vertices
def fan_triangulation(vertices, normals, material):
    triangles = []

    for index in range(2, len(vertices) - 1):
        if len(normals) > 1:
            tri = Triangle.smooth_triangle(vertices[1], vertices[index],
                                           vertices[index + 1], normals[1],
                                           normals[index], normals[index + 1])
        else:
            tri = Triangle(vertices[1], vertices[index], vertices[index + 1])
        tri.material = material
        triangles.append(tri)

    return triangles
