from rendering.scene_objects.scene_object import SceneObject

class Camera(SceneObject):
    def __init__(self, root, pos, resolution):
        super().__init__(root, pos)
        self.resolution = resolution

    def render(self):
        pass
