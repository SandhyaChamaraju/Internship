import math

class Calculator:
    def __init__(self, number):
        self.number = number

    @staticmethod
    def greet():
        print("Hello! Welcome to the Calculator application.")

    def square(self):
        return self.number ** 2

Calculator.greet()  
calc = Calculator(4)
print(f"Square: {calc.square()}")
