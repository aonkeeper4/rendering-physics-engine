from utils import vector, ray
from rendering.scene import Scene
from rendering.scene_objects import primitives, camera, lighting

root = Scene()

light = lighting.PointLight(root, vector.Vector3(3, 3, 3), 1)
camera = camera.Camera(root, vector.Vector3(0, 0, 4), (1080, 720))

sphere = primitives.Sphere(root, vector.Vector3(0, 0, 0), 1)
r, dist = sphere.bounce_specular(ray.Ray(vector.Vector3(0, 0, 2), vector.Vector3(0, 0, -1)))
print(r.normal)

root.render()



