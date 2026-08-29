class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c):
        return Complex(self.r + c.r, self.i + c.i)

    def __mul__(self, c):
        return Complex(self.r*c.r - self.i*c.i,
                       self.r*c.i + self.i*c.r)

    def show(self):
        print(self.r, "+", self.i, "i")


c1 = Complex(2, 3)
c2 = Complex(4, 5)

(c1 + c2).show()
(c1 * c2).show()
