import csv

file = "students.csv"

# Create file with headings
try:
    open(file, "r")
except:
    f = open(file, "w", newline="")
    writer = csv.writer(f)
    writer.writerow(["Roll Number", "Name", "Marks"])
    f.close()


# Add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    f = open(file, "a", newline="")
    writer = csv.writer(f)
    writer.writerow([roll, name, marks])
    f.close()

    print("Student added successfully!")


# View students
def view_students():
    f = open(file, "r")
    reader = csv.reader(f)

    for row in reader:
        print(row)

    f.close()


# Search student
def search_student():
    roll = input("Enter Roll Number: ")

    f = open(file, "r")
    reader = csv.reader(f)

    for row in reader:
        if row[0] == roll:
            print("Student Found:")
            print("Roll Number:", row[0])
            print("Name:", row[1])
            print("Marks:", row[2])
            f.close()
            return

    print("Student not found.")
    f.close()


# Delete student
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    f = open(file, "r")
    reader = csv.reader(f)
    rows = list(reader)
    f.close()

    f = open(file, "w", newline="")
    writer = csv.writer(f)

    for row in rows:
        if row[0] != roll:
            writer.writerow(row)

    f.close()

    print("Student deleted successfully!")


# Main menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
