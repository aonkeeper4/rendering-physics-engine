class Quaternion:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return "Quaternion: x: {}, y: {}, z: {}, w: {}".format(self.x, self.y, self.z, self.w)

    def __repr__(self):
        return "Quaternion: x: {}, y: {}, z: {}, w: {}".format(self.x, self.y, self.z, self.w)

    def __add__(self, other):
        return Quaternion(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Quaternion(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, other):
        return Quaternion(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)

    def __matmul__(self, other):
        return Quaternion(self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y,
                          self.w * other.y + self.y * other.w + self.z * other.x - self.x * other.z,
                          self.w * other.z + self.z * other.w + self.x * other.y - self.y * other.x,
                          self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z)

    def __truediv__(self, other):
        return Quaternion(self.x / other.x, self.y / other.y, self.z / other.z, self.w / other.w)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y or self.z != other.z or self.w != other.w

    def __neg__(self):
        return Quaternion(-self.x, -self.y, -self.z, -self.w)

    def __abs__(self):
        return Quaternion(abs(self.x), abs(self.y), abs(self.z), abs(self.w))