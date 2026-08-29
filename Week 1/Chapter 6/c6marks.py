sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total_marks = sub1 + sub2 + sub3
percentage = (total_marks / 300) * 100


if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and percentage >= 40:
    print(f"Result: PASS (Percentage: {percentage:.2f}%)")
else:
    print(f"Result: FAIL (Percentage: {percentage:.2f}%)")
