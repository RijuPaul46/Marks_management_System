import csv

def display_students():
    with open("marks.csv", "r") as file:
        reader = csv.DictReader(file)
        print("\nStudent Records\n")
        for row in reader:
            print("Roll No:", row["roll_no"])
            print("Name:", row["name"])
            print("Physics:", row["physics"])
            print("Chemistry:", row["chemistry"])
            print("Math:", row["math"])
            print("Total:", row["total"])
            print("----------------------")

def update_mark(subject):
    students = []

    with open("marks.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)

    roll = input("Enter roll number to update marks: ")
    updated_mark = input("Enter new marks: ")

    found = False

    for student in students:
        if student["roll_no"] == roll:
            student[subject] = updated_mark
            total = int(student["physics"]) + int(student["chemistry"]) + int(student["math"])
            student["total"] = str(total)
            found = True
            print("Marks Updated Successfully")

    if not found:
        print("Student not found")

    with open("marks.csv", "w", newline="") as file:
        fieldnames = ["roll_no", "name", "physics", "chemistry", "math", "total"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

print("Login as Subject Teacher")

choice = input("""
Enter:
1 for Physics
2 for Chemistry
3 for Math
""")

subject_map = {
    "1": "physics",
    "2": "chemistry",
    "3": "math"
}

if choice in subject_map:
    subject = subject_map[choice]
    display_students()
    update_mark(subject)
    print("\nUpdated Records\n")
    display_students()
else:
    print("Invalid Choice")
