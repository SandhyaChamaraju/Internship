marks_list=[]
for i in range(6):
    marks=int(input(f"enter marks of the student {i+1}: "))
    marks_list.append(marks)

marks_list.sort()
print("Sorted marks of students:",marks_list)
