class Vector:
    def __init__(self, components):
        self.components = components

    def __len__(self):
        return len(self.components)

v = Vector([7, 8, 10])

print(f"Vector components: {v.components}")
print(f"Dimension of the vector: {len(v)}")
