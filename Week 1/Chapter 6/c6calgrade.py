def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter a value between 0 and 100."
    
    if marks >= 90:
        return "Ex"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


try:
    student_marks = float(input("Enter the student's marks: "))
    grade = calculate_grade(student_marks)
    print(f"Marks: {student_marks} -> Grade: {grade}")

except ValueError:
    print("Error: Please enter a valid numerical value.")
