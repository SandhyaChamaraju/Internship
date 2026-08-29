files = ["1.txt", "2.txt", "3.txt"]

for filename in files:
    try:
        with open(filename, "r") as file:
            print(f"{filename} opened successfully.")
    except FileNotFoundError:
        print(f"{filename} is not present. Please create the file.")
