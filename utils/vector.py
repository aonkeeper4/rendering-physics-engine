class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return Vector(self.x*other, self.y*other, self.z*other)

    def __truediv__(self, other):
        return Vector(self.x/other, self.y/other, self.z/other)

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    @property
    def length(self):
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    @property
    def normalised(self):
        return self/self.length
    
    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'