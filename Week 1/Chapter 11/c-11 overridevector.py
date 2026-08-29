class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __mul__(self, v):
        return self.x * v.x + self.y * v.y

    # Overload len()
    def __len__(self):
        return 2


v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2

print("Sum of vectors:")
print(v3.x, v3.y)

print("Dot product:", v1 * v2)

print("Dimension of vector:", len(v1))
