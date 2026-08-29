with open("poems.txt", "r") as f:
    text = f.read()

if "twinkle" in text.lower():
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is not present in the file.")
