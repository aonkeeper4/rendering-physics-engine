from rendering.scene_objects import scene_object, lighting
from utils import vector, ray
import numpy as np
from PIL import Image

class Camera(scene_object.SceneObject):
    def __init__(self, root, pos, resolution):
        super().__init__(root, pos)
        self.resolution = resolution
        self.screen_distance = 1
        self.screen_size = (4, 4*self.resolution[1]/self.resolution[0])

    def render(self, scene):
        # https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-overview/ray-tracing-rendering-technique-overview
        # depth buffer to order objs correctly
        # also shadows
        w, h = self.resolution
        frame_buffer = np.zeros((h, w, 3), dtype=np.uint8)
        for j in range(self.resolution[1]):
            for i in range(self.resolution[0]):
                for start_obj in scene.objects:
                    if isinstance(start_obj, lighting.LightSource):
                        continue
                    ray = self.build_camera_ray(i, j)
                    obj = start_obj
                    total_dist = 0.001
                    # i have no idea whether this inner loop is even needed
                    while ray and total_dist:
                        try:
                            ray, dist = obj.bounce_specular(ray)
                        except TypeError:
                            ray = False
                            break
                        else:
                            # print(f"hit {type(obj)}")
                            # diffuse light
                            to_light = vector.Vector3.normalised(ray.origin - scene.light.pos)
                            cos_angle = obj.normal(ray.origin).dot(to_light)
                            # print(cos_angle)
                            diffuse = 200 * (1 if cos_angle >= 1 else (0 if cos_angle <= 0 else cos_angle))
                            frame_buffer[j, i] = [diffuse, diffuse, diffuse]
                        for new_obj in scene.objects:
                            if new_obj == start_obj:
                                continue
                            if new_obj.intersect(ray):
                                _, dist = new_obj.intersect(ray)
                                total_dist += dist
                                if isinstance(new_obj, lighting.LightSource):
                                    # print("light source found")
                                    # # brightness is inversely proportional to the square of the distance
                                    # brightness = 255/(total_dist**2*0.2)
                                    brightness = 255
                                    frame_buffer[j, i] = [brightness, brightness, brightness]
                                    ray = False
                                    break
                                obj = new_obj
                        break
                        total_dist += dist
                    # print("moving to new pixel")

        img = Image.fromarray(frame_buffer, 'RGB')
        img.save('render.png')
        print("done!")

    def build_camera_ray(self, i, j):
        world_i = (i * self.screen_size[0] / self.resolution[0]) - self.screen_size[0]/2
        world_j = (j * self.screen_size[1] / self.resolution[1]) - self.screen_size[1]/2
        direction = vector.Vector3(world_i, world_j, self.screen_distance) - self.pos
        return ray.Ray(self.pos, vector.Vector3.normalised(direction))
