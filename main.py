from utils import vector
from rendering.scene import Scene
from rendering.scene_objects import primitives, camera, lighting

root = Scene()

light = lighting.PointLight(root, vector.Vector3(2, 2, 2))
camera = camera.Camera(root, vector.Vector3(0, 0, 2))

sphere = primitives.Sphere(root, vector.Vector3(0, 0, 0), 1)



