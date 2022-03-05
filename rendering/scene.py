from rendering.scene_objects import camera, lighting

class Scene:
    def __init__(self):
        self.objects = []
        self.camera = None
        self.light = None

    def add(self, obj):
        if isinstance(obj, lighting.LightSource):
            self.light = obj
        if isinstance(obj, camera.Camera):
            self.camera = obj
        else:
            self.objects.append(obj)

    def render(self):
        self.camera.render(self)