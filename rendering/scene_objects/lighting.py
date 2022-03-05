from rendering.scene_objects.scene_object import SceneObject
from rendering.render_utils import sphere_line_intersection

class LightSource(SceneObject):
    def __init__(self, root, pos):
        super().__init__(root, pos)

class PointLight(LightSource):
    def __init__(self, root, pos, radius):
        super().__init__(root, pos)
        self.radius = radius

    def intersect(self, ray):
        intersection_points = sphere_line_intersection(ray.origin, ray.normal, self.pos, self.radius)
        try: primary = intersection_points[0]
        except IndexError: return tuple()
        return intersection_points, (primary - ray.origin).length

class AreaLight(LightSource):
    def __init__(self, root, pos):
        super().__init__(root, pos)