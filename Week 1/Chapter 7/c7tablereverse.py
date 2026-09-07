n = int(input("Enter the number: "))

print(f"\nMultiplication Table of {n} in Reverse Order:")
for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")
