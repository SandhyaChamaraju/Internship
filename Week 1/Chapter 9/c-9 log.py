with open("log.txt", "r") as file:
    data = file.read()

if "python" in data.lower():
    print("The log file contains 'python'.")
else:
    print("The log file does not contain 'python'.")
