from lights import PointLight
from shapes import Cone, Cube, Cylinder, Plane, Sphere

from .camera import Camera
from .world import World

_TYPE_MAP = {
    'camera': Camera.from_yaml,
    'light': PointLight.from_yaml,
    'cone': Cone.from_yaml,
    'cube': Cube.from_yaml,
    'cylinder': Cylinder.from_yaml,
    'plane': Plane.from_yaml,
    'sphere': Sphere.from_yaml
}


def scene_from_yaml(data):
    scene = [None, World()]
    definitions = {}

    for item in data:
        if 'add' in item:
            preprocess_definitions(definitions, item)
            add_to_scene(scene, item)

        if 'define' in item:
            add_to_definitions(definitions, item)

    return tuple(scene)


def preprocess_definitions(definitions, item):
    if 'material' in item and isinstance(item['material'], str):
        name = item['material']
        item['material'] = definitions.get(name)

    if 'transform' in item:
        new = []
        old = item['transform']
        for transformation in old:
            if isinstance(transformation,
                          str) and transformation in definitions:
                new.extend(definitions.get(transformation))
            else:
                new.append(transformation)
        item['transform'] = new


def add_to_scene(scene, item):
    item_type = item['add']

    parse_method = _TYPE_MAP.get(item_type)
    if parse_method is None:
        raise ValueError(f"Unknown type '{item_type}'")

    if item_type == 'camera':
        scene[0] = parse_method(item)
    elif item_type == 'light':
        scene[1].add_light(parse_method(item))
    else:
        scene[1].objects.append(parse_method(item))


def add_to_definitions(definitions, item):
    name = item['define']

    parent_values = None

    if 'extend' in item:
        parent_name = item['extend']
        if not parent_name in definitions:
            raise ValueError(f"Unknown parent definition '{parent_name}'")
        parent_values = definitions.get(parent_name)

    definitions[name] = merge_definitions(parent_values, item['value'])


def merge_definitions(parent, child):
    if not parent:
        return child

    if isinstance(child, list):
        return parent.extend(child)

    return {**parent, **child}
