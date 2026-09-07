def print_pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))

n = 3
print_pyramid(n)
