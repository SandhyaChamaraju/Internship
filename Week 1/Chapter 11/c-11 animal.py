class Animals:
    def __init__(self, name):
        self.name = name


class Pets(Animals):
    def show(self):
        print("This is a pet.")


class Dog(Pets):
    def bark(self):
        print("Woof! Woof!")


# Create a Dog object
d = Dog("Tommy")

print("Dog's name:", d.name)
d.show()
d.bark()
