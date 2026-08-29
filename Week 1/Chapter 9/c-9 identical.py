file1 = open("this.txt", "r")
file2 = open("copy.txt", "r")

content1 = file1.read()
content2 = file2.read()

if content1 == content2:
    print("Both files are identical.")
else:
    print("Both files are not identical.")

file1.close()
file2.close()
