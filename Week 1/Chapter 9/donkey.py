filename = "file.txt"

with open(filename, "r") as file:
    data = file.read()

data = data.replace("Donkey", "######")

with open(filename, "w") as file:
    file.write(data)

print("Replacement completed successfully.")
