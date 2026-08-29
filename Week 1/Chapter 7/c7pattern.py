def print_pattern(n):
    for i in range(n):
        for j in range(n):
            # Print star if it is on the boundary (first/last row or column)
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Test with n = 3
print_pattern(3)
