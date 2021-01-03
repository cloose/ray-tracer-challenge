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
