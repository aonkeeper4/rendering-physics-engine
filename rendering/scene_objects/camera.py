from rendering.scene_objects.scene_object import SceneObject
from utils import vector, ray

# class FrameBuffer:
#     def __init__(self, width, height, framebuffer=[]):
#         self.buffer = framebuffer
#         self.width = width
#         self.height = height
#         self.n = 0

#     def __iter__(self):
#         self.n = 0
#         return self

#     def __next__(self):
#         if self.n <= len(self.buffer):
#             result = (self.n % self.width, self.n // self.width, self.buffer[self.n])
#             self.n += 1
#             return result
#         else:
#             raise StopIteration

class Camera(SceneObject):
    def __init__(self, root, pos, resolution):
        super().__init__(root, pos)
        self.resolution = resolution
        self.screen_distance = 1
        self.screen_size = (1, self.resolution[1]/self.resolution[0])

    def render(self, scene):
        framebuffer = []
        for j in range(self.resolution[1]):
            for i in range(self.resolution[0]):
                for obj in scene.objects:
                    ray = self.build_camera_ray(i, j)
                    if obj.intersect(ray):
                        # framebuffer[j * self.resolution[0] + i] = 1;
                        print("#", end="")
                    else:
                        # framebuffer[j * self.resolution[0] + i] = 0;
                        print(" ", end="")
            print("\n", end="")

    def build_camera_ray(self, i, j):
        world_i = i * self.screen_size[0] / self.resolution[0]
        world_j = j * self.screen_size[1] / self.resolution[1]
        direction = self.pos - vector.Vector3(world_i, world_j, self.screen_distance)
        return ray.Ray(self.pos, vector.Vector3.normalised(direction))
