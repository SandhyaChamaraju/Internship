n = int(input("Enter a number: "))

table = [n * i for i in range(1, 11)]

with open("Table1.txt", "w") as f:
    for i in table:
        f.write(str(i) + "\n")

print("Table stored in Table1.txt")
