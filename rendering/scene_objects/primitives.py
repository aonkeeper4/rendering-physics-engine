class Primitive(SceneObject):
    def __init__(self, pos):
        super().__init__(pos)

    def intersect(self, obj):
        pass

class Sphere(Primitive):
    def __init__(self, pos, radius):
        super().__init__(pos)
        self.radius = radius

    @staticmethod
    def sphere_line_intersection(o, u, c, r):
            nabla = (u.dot(o-c))**2 - ((o-c).length**2-r**2)
            if nabla < 0: return None #oh god my eyes
            d0 = -(u.dot(o-c)) + sqrt(nabla)
            d1 = -(u.dot(o-c)) - sqrt(nabla)
            v0 = o + u*d0
            v1 = o + u*d1
            if nabla == 0: return v0
            else: return v0, v1

    def intersect(self, obj):
        if isinstance(obj, Ray):
            return Sphere.sphere_line_intersection(obj.origin, obj.normal, self.pos, self.radius)

class Mesh(Primitive):
    pass