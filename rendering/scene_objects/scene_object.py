class SceneObject:
    def __init__(self, root, pos):
        self.root = root
        self.pos = pos
        self.root.add(self)