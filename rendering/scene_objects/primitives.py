from rendering.scene_objects.scene_object import SceneObject
from utils import vector, ray
from rendering.render_utils import get_specular_reflection_from_normal, get_diffuse_reflection_from_normal, sphere_line_intersection

class Primitive(SceneObject):
    def __init__(self, root, pos):
        super().__init__(root, pos)

    def intersect(self, obj):
        pass

class Sphere(Primitive):
    def __init__(self, root, pos, radius):
        super().__init__(root, pos)
        self.radius = radius

    def intersect(self, r):
        intersection_points = sphere_line_intersection(r.origin, r.normal, self.pos, self.radius)
        try: primary = intersection_points[0]
        except IndexError: return tuple()
        return intersection_points, (primary - r.origin).length

    def bounce_specular(self, r):
        intersection_points = sphere_line_intersection(r.origin, r.normal, self.pos, self.radius)
        try: primary = intersection_points[0]
        except IndexError: return False
        normal = primary - self.pos
        reflection = get_specular_reflection_from_normal(r.normal, vector.Vector3.normalised(normal))
        return ray.Ray(primary, reflection), (primary - r.origin).length

    def bounce_diffuse(self, r):
        intersection_points = sphere_line_intersection(r.origin, r.normal, self.pos, self.radius)
        try: primary = intersection_points[0]
        except IndexError: return False
        normal = primary - self.pos
        reflection = get_diffuse_reflection_from_normal(r.normal, vector.Vector3.normalised(normal))
        return ray.Ray(primary, reflection), (primary - r.origin).length
        
class Mesh(Primitive):
    pass