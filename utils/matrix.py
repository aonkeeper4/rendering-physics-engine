class Matrix4x4:
    def __init__(self, value):
        assert len(value) == 16
        self.value = value

    def dimensionalise(self):
        return [self.value[i:i+4] for i in range(0, 16, 4))]

    def vectorise(self):
        return [self.value[i::4] for i in range(0, 4))]

    def from_vectorised(vectorised):
        pass

    def __add__(self, other):
        return Matrix4x4(list(map(lambda x, y: x + y, self.value, other.value)))

    def __sub__(self, other):
        return Matrix4x4(list(map(lambda x, y: x - y, self.value, other.value)))

    def __mult__(self, other):
        assert isinstance(other, (Vector4, Matrix4x4))
        if isinstance(other, Vector4):
            pass