filename = input("Enter the file name: ")

with open(filename, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))
