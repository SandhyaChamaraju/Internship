a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    print(a / b)
except ZeroDivisionError:
    print("Infinite")
