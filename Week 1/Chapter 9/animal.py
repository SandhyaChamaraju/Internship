filename = "file2.txt"

words = ["Donkey", "Monkey", "Tiger", "Lion"]

with open(filename, "r") as file:
    data = file.read()

for word in words:
    data = data.replace(word, "######")

with open(filename, "w") as file:
    file.write(data)

print("All words have been censored.")
