from rendering.scene_objects.scene_object import SceneObject
from utils.ray import Ray
from rendering.utils import get_vector_reflection_from_normal, sphere_line_intersection

class Primitive(SceneObject):
    def __init__(self, root, pos):
        super().__init__(root, pos)

    def intersect(self, obj):
        pass

class Sphere(Primitive):
    def __init__(self, root, pos, radius):
        super().__init__(root, pos)
        self.radius = radius

    def intersect(self, ray):
        intersection_points = sphere_line_intersection(ray.origin, ray.normal, self.pos, self.radius)
        return intersection_points

    def bounce(self, ray):
        intersection_points = sphere_line_intersection(ray.origin, ray.normal, self.pos, self.radius)
        try: primary = intersection_points[0]
        except IndexError: return False
        normal = self.pos - primary
        reflection = get_vector_reflection_from_normal(ray.normal, normal)
        return Ray(primary, reflection)
        
class Mesh(Primitive):
    pass