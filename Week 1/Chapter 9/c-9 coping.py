with open("this.txt", "r") as file:
    data = file.read()

with open("copy.txt", "w") as file:
    file.write(data)

print("File copied successfully.")
