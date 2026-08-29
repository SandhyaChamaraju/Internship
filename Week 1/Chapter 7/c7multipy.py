# Prompt user for input and convert it to an integer
number = int(input("Enter a number to print its multiplication table: "))

print(f"\nMultiplication Table for {number}:")
# Loop from 1 to 10
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
