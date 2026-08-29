# Prompt the user to input an integer
num = int(input("Enter a number: "))

# Initialize the factorial variable to 1
factorial = 1

# Factorials are not defined for negative numbers
if num < 0:
    print("Factorial does not exist for negative numbers.")
# The factorial of 0 is 1
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # Loop from 1 to num (num + 1 is exclusive)
    for i in range(1, num + 1):
        factorial *= i
        
    print(f"The factorial of {num} is {factorial}")
