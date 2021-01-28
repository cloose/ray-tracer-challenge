class Intersection:
    def __init__(self, t, obj, u=None, v=None):
        self.t = t
        self.object = obj
        self.u = u
        self.v = v

    def __lt__(self, other):
        return self.t < other.t


def hit(xs):
    result = None
    for i in xs:
        if i.t > 0 and (result is None or i.t < result.t):
            result = i
    return result


def shadow_hit(xs):
    result = None
    for i in filter(lambda x: x.t > 0 and x.object.cast_shadow, xs):
        if result is None or i.t < result.t:
            result = i
    return result
