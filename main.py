from utils import matrix, ray
from rendering.scene import Scene
from rendering.scene_objects import primitives, camera, lighting

root = Scene()

light = lighting.PointLight(root, matrix.Vector([8, 4, 4]), 2)
cam = camera.Camera(root, matrix.Vector([0, 0, 4]), (54, 36))

sphere1 = primitives.Sphere(root, matrix.Vector([0, -1.5, -2]), 1)
sphere1 = primitives.Sphere(root, matrix.Vector([0, 1.5, -2]), 1)
sphere3 = primitives.Sphere(root, matrix.Vector([1.25, 0, 0]), 1)
sphere4 = primitives.Sphere(root, matrix.Vector([-1.25, 0, 0]), 1)

root.render()