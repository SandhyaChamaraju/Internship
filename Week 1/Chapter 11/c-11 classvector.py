class Vector:
    def __init__(self, v):
        self.v = v

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.v, other.v)])

    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.v, other.v))

    def show(self):
        print(self.v)


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

(v1 + v2).show()
print(v1 * v2)
