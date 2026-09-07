import math

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def square_root(self):
        return math.sqrt(self.number)

calc = Calculator(9)
print(f"Square: {calc.square()}")        
print(f"Cube: {calc.cube()}")            
print(f"Square Root: {calc.square_root()}") 

