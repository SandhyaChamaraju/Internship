unique_numbers = []

print("Please enter 8 numbers:")

for i in range(8):
    num = int(input(f"Enter number {i + 1}: "))
    
    if num not in unique_numbers:
        unique_numbers.append(num)

# Display the unique numbers
print("\nThe unique numbers are:")
print(unique_numbers)
