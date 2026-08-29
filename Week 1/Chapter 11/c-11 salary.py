class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary - self.salary) / self.salary) * 100


# Create an employee object
emp = Employee(50000, 10)

print("Salary:", emp.salary)
print("Increment:", emp.increment)
print("Salary after increment:", emp.salaryAfterIncrement)

# Using the setter
emp.salaryAfterIncrement = 60000

print("New increment:", emp.increment)
print("New salary after increment:", emp.salaryAfterIncrement)
