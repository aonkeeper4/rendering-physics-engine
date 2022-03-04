from rendering.scene_objects.camera import Camera

class Scene:
    def __init__(self):
        self.objects = []
        self.camera = None

    def add(self, obj):
        if isinstance(obj, Camera):
            self.camera = obj
        else:
            self.objects.append(obj)

    def render(self):
        self.camera.render(self)