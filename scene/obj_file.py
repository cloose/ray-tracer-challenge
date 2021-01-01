from shapes import Group


class ObjFile:
    def __init__(self):
        self.ignored = 0
        self.vertices = [None]
        self.groups = {"default": Group()}

    def obj_group(self):
        group = Group()
        group.children.extend(self.groups.values())
        return group
