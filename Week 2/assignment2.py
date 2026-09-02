f = open("text.txt", "r")

text = f.read()

print("Words:", len(text.split()))
print("Lines:", len(text.splitlines()))
print("Characters:", len(text))

f.close()
