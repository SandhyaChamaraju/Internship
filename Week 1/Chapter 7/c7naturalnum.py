# Program to find the sum of first n natural numbers

# Take input from the user
n = int(input("Enter a positive integer (n): "))

# Initialize sum and counter
total_sum = 0
i = 1

# The while loop runs until i is greater than n
while i <= n:
    total_sum += i  # Add the current value of i to the total sum
    i += 1          # Increment i by 1 for the next iteration

# Print the final result
print(f"The sum of the first {n} natural numbers is: {total_sum}")
