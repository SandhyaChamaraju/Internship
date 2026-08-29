def print_pattern(n):
    for i in range(n, 0, -1):
        print("  ".join(["*"] * i))

# Example usage for n = 3
print_pattern(3)
