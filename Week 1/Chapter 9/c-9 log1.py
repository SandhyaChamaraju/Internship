with open("log1.txt", "r") as file:
    lines = file.readlines()

for line_number, line in enumerate(lines, start=1):
    if "python" in line.lower():
        print("Python is present on line number:", line_number)
