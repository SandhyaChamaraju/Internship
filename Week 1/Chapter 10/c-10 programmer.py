class Programmer:
    company = "Microsoft"

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def get_details(self):
        print(f"Programmer: {self.name}")
        print(f"Company: {self.company}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,}\n")

# Creating object instances
p1 = Programmer("Alisha", "Azure Cloud", 120000)
p2 = Programmer("Rohan", "Developer Tools", 115000)

p1.get_details()
p2.get_details()
