class EzdVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"({self.x}, {self.y})")


class Vector3D(EzdVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        print(f"({self.x}, {self.y}, {self.z})")


# Create objects
v1 = EzdVector(2, 3)
v2 = Vector3D(2, 3, 4)

v1.display()
v2.display()
