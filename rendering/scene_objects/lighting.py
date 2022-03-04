from rendering.scene_objects.scene_object import SceneObject

class LightSource(SceneObject):
    def __init__(self, root, pos):
        super().__init__(root, pos)

class PointLight(LightSource):
    def __init__(self, root, pos):
        super().__init__(root, pos)

class AreaLight(LightSource):
    def __init__(self, root, pos):
        super().__init__(root, pos)