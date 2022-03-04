from utils import vector, ray
from rendering.scene import Scene
from rendering.scene_objects import primitives, camera, lighting

root = Scene()

light = lighting.PointLight(root, vector.Vector3(2, 2, 2))
camera = camera.Camera(root, vector.Vector3(0, 0, 2), (1080, 720))

sphere = primitives.Sphere(root, vector.Vector3(0, 0, 0), 1)
sphere.bounce(ray.Ray(vector.Vector3(0, 0, 2), vector.Vector3(0, 0, -1)))



