def find_greatest(a, b, c):
    """
    Function to find the greatest of three numbers.
    It takes three numbers as arguments and returns the largest one.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calling the function and storing the result
result = find_greatest(num1, num2, num3)

print(f"The greatest number is: {result}")
