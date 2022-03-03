from math import sqrt
from utils import vector, matrix, quaternion
from rendering.scene_objects import primitives, camera, lighting
import PIL

light = lighting.PointLight(Vector(2, 2, 2))
camera = camera.Camera(vector.Vector(0, 0, 2))

sphere = primitives.Sphere(vector.Vector(0, 0, 0), 1)



