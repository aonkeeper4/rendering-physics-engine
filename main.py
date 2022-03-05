from utils import vector, ray
from rendering.scene import Scene
from rendering.scene_objects import primitives, camera, lighting

root = Scene()

<<<<<<< HEAD
light = lighting.PointLight(root, vector.Vector3(0, 4, 4), 2)
=======
light = lighting.PointLight(root, vector.Vector3(2, 4, 4), 2)
>>>>>>> 556de3d42b46cde4012bc3e9075652ecf0837336
cam = camera.Camera(root, vector.Vector3(0, 0, 4), (108, 72))

sphere1 = primitives.Sphere(root, vector.Vector3(1.25, 0, 0), 1)
sphere2 = primitives.Sphere(root, vector.Vector3(-1.25, 0, 0), 1)

root.render()