def print_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print stars
        print("*" * (2 * i - 1))

# Given input
n = 3
print_pyramid(n)
